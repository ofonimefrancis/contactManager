# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Contact Model with name and email fields
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    #created_at = models.DateTimeField('date created')

    def __str__(self):
        return self.name