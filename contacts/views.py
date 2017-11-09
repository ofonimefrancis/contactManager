# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from .forms import ContactsForm

from django.shortcuts import render

# Create your views here.
def index(request):
    template = loader.get_template("contacts/index.html")
    return HttpResponse(template.render({}, request))

def listContacts(request):
    #latest_contacts = Contact.objects.order_by('-date_created')[:5]
    template = loader.get_template("contacts/list.html")
    return HttpResponse(template.render({}, request))

def addContacts(request):
    form = ContactsForm()
    context = {
        'form' : form
    }
    template = loader.get_template("contacts/add.html")
    return HttpResponse(template.render(context, request))
