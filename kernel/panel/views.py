from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from painless.decorators import confirm_password

# Create your views here.

class PanelView(generic.TemplateView):
    template_name = 'panel/index.html'
    

    #additional information
    title = 'خانه'

