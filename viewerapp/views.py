from django.shortcuts import render

from .credentials import ZENDESK_PASSWORD, ZENDESK_USERNAME, ZENDESK_SUBDOMAIN
from .models import Ticket
from django.core.paginator import Paginator

from django.http import HttpResponse

import requests

# Create your views here.

def index(request):
    #tickets = Ticket.objects.order_by('-created_at')[:5]
    tickets = requests.get("https://{0}.zendesk.com/api/v2/tickets/".format(ZENDESK_SUBDOMAIN), auth=(ZENDESK_USERNAME,ZENDESK_PASSWORD))

    if tickets.status_code != requests.codes.ok:
        return render(request,'login_error.html',{})  
    tickets = tickets.json()
    paginator = Paginator(tickets['tickets'],25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',{'page_obj':page_obj})
    

def ticket_by_id(request, ticket_id):
    ticket = requests.get("https://{0}.zendesk.com/api/v2/tickets/{1}.json".format(ZENDESK_SUBDOMAIN,ticket_id), auth=(ZENDESK_USERNAME,ZENDESK_PASSWORD)).json()
    if ticket.status_code != requests.codes.ok:
        return render(request,'page_error.html',{}) 
    return render(request, 'ticket_by_id.html', ticket)