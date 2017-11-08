# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Index Page")

def listContacts(request):
    return HttpResponse("List all contacts")

def addContacts(request):
    return HttpResponse("Adds a contact")
