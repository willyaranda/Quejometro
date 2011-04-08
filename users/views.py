# coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth import authenticate, login

from django.core.context_processors import csrf
from django.shortcuts import render_to_response

from users.models import UserProfile
from users.forms import UserProfileForm

# l10n
from django.utils.translation import ugettext_lazy as _

def new(request):
    form = RegistrationForm(request.POST, request.FILES)
    
    if (checkEmail(form.email)):
        #bien
        return true
    else:
        #mal
        return false
    
    
def login(request):
    # If we submitted the form...
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('login.html', c)
            #else:
                # Return a 'disabled account' error message
    else:
        return render_to_response('login.html', c)
        # Return an 'invalid login' error message.

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")