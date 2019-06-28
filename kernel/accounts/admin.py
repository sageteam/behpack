from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .actions import make_active
from .actions import make_deactive


from .models import User
from .models import Profile



# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

    fields = [('role', 'phone_number', 'national_code')]



@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


    list_display = ('email', 'last_name', 'is_active', 'get_phone_number', 'get_role', 'get_national_code')
    inlines = (ProfileInline,)

    search_fields = ('email', 'profile__national_code', 'profile__phone_number', 'last_name')
    list_filter = ('profile__role', 'is_active', 'is_staff')

    actions = [make_active, make_deactive]
    ordering = ('email',)


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


    def get_role(self, instance):
        role_number = instance.profile.role
        if role_number == 3:
            return 'Supervisor'
        elif role_number == 2:
            return 'Genius'
        else:
            return 'Member'


    def get_phone_number(self, instance):
        return instance.profile.phone_number


    def get_national_code(self, instance):
        return instance.profile.national_code

    get_role.short_description = 'Role'
    get_phone_number.short_description = 'Phone Number'

