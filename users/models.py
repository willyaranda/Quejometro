# coding=utf-8
from django.db import models
#Extending basic User auth models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

#Email domain for checking the emails
EMAIL_DOMAIN = "alumnos.nebrija.es"

class UserProfile(models.Model):
    #Required, maps our UserProfile class to django User models
    user = models.ForeignKey(User, unique=True)
    
    slug = models.SlugField(_(u"Slug"), max_length=50)
    votes = models.ManyToManyField('claims.Claim', null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.nick)
        
    def checkEmail(email):
        #FIXME: chage alumnos.nebrija.es to the EMAIL_DOMAIN constrain
        if re.match('[a-zA-Z0-9+_\-\.]+@alumnos.nebrija.es', b):
            return true
        return false
