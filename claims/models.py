# coding=utf-8
from django.db import models

from django.utils.translation import ugettext_lazy as _

import datetime

#Category list (with studies)
CATEGORY_LIST = (
    ('GENERAL', 'General'),
    ('CAFETERIA', 'Cafetería'),
    ('BIBLIOTECA', 'Biblioteca'),
    ('AULAS', 'Aulas'),
    #Studies list
    ('INGINFSUP', 'Ingeniería Informática'),
    ('INGINFTECSIS', 'Ingeniería técnica en informática de sistemas'),
    ('INGINFTECGES', 'Ingeniería técnica en informática de gestión'),
    ('GRADOINF', 'Grado en Informática'),
    ('INGINDSUP', 'Ingeniería Industrial'),
    #('', ''),
)

class Claim(models.Model):
    title = models.CharField(_("Title"), max_length=140)
    slug = models.SlugField(_("Slug"), max_length=50, unique=True)
    description = models.TextField(_("Description"))
    category = models.CharField(_("Category"), max_length=100, choices=CATEGORY_LIST)
    creator = models.ForeignKey('users.UserProfile')
    
    #Optional (or blank at creation time)
    votes = models.IntegerField(_("Votes"), default=0, blank=True)
    creationDateTime = models.DateTimeField(_("Creation date"), auto_now=True)
    latestEdition = models.DateTimeField(_("Last edition time"), auto_now=True)
    
    #Tracking fields
    accepted = models.BooleanField(_("Claim accepted"), default=False, help_text=_("Has the claim been accepted?"))
    sent = models.BooleanField(_("Claim sent"), default=False, help_text=_("Has the claim been sent?"))
    status = models.TextField(_("Status"), blank=True, help_text=_("Actual status of the claim. For tracking purposes"))
    resolved = models.BooleanField(_("Is the petition resolved?"), default=False, blank=True)

    def __unicode__(self):
        return u'%s' % (self.title)
