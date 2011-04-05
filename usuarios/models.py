# coding=utf-8
from django.db import models

from django.utils.translation import ugettext_lazy as _

#Listado de categorías (con carreras) para usarla en las opciones.
LISTA_DE_CATEGORIAS = (
    ('GENERAL', 'General'),
    ('CAFETERIA', 'Cafetería'),
    ('BIBLIOTECA', 'Biblioteca'),
    ('CLASES', 'Clases'),
    #Listado de carreras
    ('INGINFSUP', 'Ingeniería Informática'),
    ('INGINFTECSIS', 'Ingeniería técnica en informática de sistemas'),
    ('INGINFTECGES', 'Ingeniería técnica en informática de gestión'),
    ('GRADOINF', 'Grado en Informática'),
    ('INGINDSUP', 'Ingeniería Industrial'),
    #('', ''),
)

class Usuario(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=50, blank=True)
    slug = models.SlugField(_("Nombre corto"), max_length=50)
    nick = models.CharField(_("Nick"), max_length=50)
    correo = models.EmailField(_("Correo"))
    carrera = models.CharField(_("Carrera"), max_length=100, choices=LISTA_DE_CATEGORIAS)

    def __unicode__(self):
        return u'%s' % (self.name)

    
#Email domain for checking the emails
EMAIL_DOMAIN = "alumnos.nebrija.es"