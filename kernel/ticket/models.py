from django.db import models

import secrets

from accounts.models import User
from painless import functions as func
# Create your models here.

##############################
#######     TICKET     #######
##############################


class TicketDepartment(models.Model):
    department_name = models.CharField( null = True, max_length = 20)
    users = models.ManyToManyField(User, verbose_name = 'users in dept', help_text = 'list of users in a department')

    verbose_name = 'company department'
    verbose_name_plural = 'company department'


class Ticket(models.Model):

    LOW = '1'
    NORMAL = '2'
    HIGH = '3'
    URGANT = '4'

    SEVERITY = (
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
        (URGANT, 'Urgant')
    )

    CLOSED = '0'
    OPEN = '1'

    STATUS = (
        (CLOSED, 'Closed'),
        (OPEN, 'Open')
    )

    sku = models.CharField(max_length = 15, default = secrets.token_urlsafe(8), help_text = 'Unique code for refrence to supervisors' )
    
    title = models.CharField(blank = False, null = False, max_length = 20)
    message = models.TextField(blank = False, null = False, max_length=526)
    submited_by = models.ForeignKey('accounts.User', on_delete = models.SET_NULL, null = True)
    department = models.ForeignKey('TicketDepartment', null = True, on_delete = models.SET_NULL)
    reply = models.ForeignKey('TicketReply', null = True, on_delete = models.SET_NULL)
    
    priority = models.CharField( choices = SEVERITY, default = SEVERITY[0], max_length = 1)
    status = models.CharField( max_length = 1, choices = STATUS, null = False, default = STATUS[0])
    order_date = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-priority', '-status', '-order_date')



class TicketAttachment(models.Model):
    name = models.CharField(max_length = 50, null = True)
    file_address = models.CharField(max_length = 526, null = True)
    ticket_attachment = models.ForeignKey('Ticket', null = True, on_delete = models.SET_NULL, blank = True)
    reply_attachment = models.ForeignKey('TicketReply', null = True, on_delete = models.SET_NULL, blank = True)


class TicketReply(models.Model):
    ANSWERED = '202'
    QUESTION = '201'

    REQUEST_TYPE = (
        (ANSWERED, 'Answered'),
        (QUESTION, 'Request')
    )

    message = models.TextField(null = True, max_length=526)

    attachments = models.ForeignKey('TicketAttachment', null = True, on_delete = models.SET_NULL)
    request_type = models.CharField( choices = REQUEST_TYPE, null = True, max_length = 3)
    submited_by = models.ForeignKey('accounts.User', on_delete = models.SET_NULL, null = True)
    submit_date = models.DateTimeField(auto_now = True)



    class Meta:
        ordering = ('request_type', 'submit_date',)
        verbose_name = 'Ticket Reply Message'
        verbose_name_plural = 'Ticket Reply Messages'