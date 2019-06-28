from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login

from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import SignUpForm
from .forms import SignInForm

from django.views.generic.edit import UpdateView
from .forms import ConfirmPasswordForm
from kernel import settings

from painless.decorators import confirm_password

# Create your views here.

class ConfirmPasswordView(UpdateView):
    form_class = ConfirmPasswordForm
    template_name = 'registration/login.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return self.request.get_full_path()



class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/login.html'

    title = 'ثبت نام اعضاء به داشبورد'
    button = 'ثبت نام کن'



class SignInView(generic.FormView):
    success_url = '/panel'
    form_class = SignInForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/login.html'

    title = 'ورود اعضاء به داشبورد'
    button = 'وارد شو'
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/panel')
            else:
                return HttpResponse('Inactive user')
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
        

        return render(request, 'registration/login.html')


class SignOutView(generic.RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(SignOutView, self).get(request, *args, **kwargs)

