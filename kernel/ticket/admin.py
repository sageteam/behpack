from django.contrib import admin

from .models import Ticket
from .models import TicketReply
from .models import TicketDepartment
from .models import TicketAttachment

##############################
#######     TICKET     #######
##############################

@admin.register(TicketAttachment)
class TicketAttachmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TicketDepartment)
class TicketDepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name',)


@admin.register(TicketReply)
class TicketReplyAdmin(admin.ModelAdmin):
    list_display = ('message', 'submited_by',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('sku', 'title', 'get_department', 'priority', 'status', 'order_date')
    list_filter = ('status', 'priority', 'department__department_name', 'order_date')
    search_fields = ('title', 'message', 'reply__message', 'sku')
    empty_value_display = '-empty-'
    #inlines = (TicketDepartmentInline, TicketReplyInline)


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(TicketAdmin, self).get_inline_instances(request, obj)
    

    def get_department(self, instance):
        return instance.department.department_name

    get_department.short_description = 'Department'