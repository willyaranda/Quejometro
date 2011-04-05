# coding=utf-8
from django.db import models

from django.utils.translation import ugettext_lazy as _

import datetime

class Queja(models.Model):
    titulo = models.CharField(_("Nombre"), max_length=140)
    slug = models.SlugField(_("Nombre corto"), max_length=50, unique=True)
    descripcion = models.TextField(_("Descripcion"))
    votos = models.IntegerField(_("Votos"), default=0, blank=True)
    diaCreacion = models.DateTimeField(auto_now=True)
    #Campos para el tracking
    aceptada = models.BooleanField(_("Propuesta aceptada"), default=False, help_text=_("Ha sido aceptada la propuesta?"))
    enviada = models.BooleanField(_("Propuesta enviada"), default=False, help_text=_("Ha sido enviada la propuesta?"))
    estado = models.TextField(_("Estado"), blank=True, help_text=_("Estado actual de la peticion, para hacer seguimiento"))
    resuelta = models.BooleanField(_("Peticion resuelta"), default=False, blank=True)

    def __unicode__(self):
        return u'%s' % (self.titulo)
