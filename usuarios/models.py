from django.db import models

from django.utils.translation import ugettext_lazy as _

class Usuario(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=50, blank=True)
    nick = models.CharField(_("Nick"), max_length=50, blank=True)
    slug = models.SlugField(_("Nombre corto"), max_length=50)
    correo = models.EmailField(_("Correo"))
    
    def __unicode__(self):
        return u'%s' % (self.name)
    