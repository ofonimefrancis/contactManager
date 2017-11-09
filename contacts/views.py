# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import ContactsForm

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render 

import logging 


logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    template = loader.get_template("contacts/index.html")
    return HttpResponse(template.render({}, request))

def list(request):
    from contacts.models import Contact
    all_contacts = Contact.objects.all()
    template = loader.get_template("contacts/list.html")
    return HttpResponse(template.render({ "contacts": all_contacts}, request))

def add(request):
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact Successfully added")
        else:
            messages.error(request, "Unable to Create new contact")

        return HttpResponseRedirect(redirect_to="/add")

    else:
        form = ContactsForm()
    
    template = loader.get_template("contacts/add.html")
    return HttpResponse(template.render({"form": form}, request))


