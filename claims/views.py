# coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template import Context
from django.utils.translation import ugettext_lazy as _

#Our classes, models, forms...
from claims.models import Claim
from users.models import UserProfile
from claims.forms import ClaimForm


def index(request):
    #Limit the 5 most voted...
    claimList = Claim.objects.order_by('-votes')[:5]
    data = {
        'claims': claimList,
    }
    return render_to_response('index.html', data, context_instance=RequestContext(request))


def detail(request, id, slug):
    claim = get_object_or_404(Claim, id=id)
    data = {
        'claim': claim,
    }
    return render_to_response('detail.html', data, context_instance=RequestContext(request))


def new(request):
    if request.method == 'POST':
        claim = ClaimForm(request.POST)
        if claim.is_valid():
            claim.save()
            c = get_object_or_404(Claim, slug=claim.cleaned_data['slug'])
            #Showing message and redirecting to now added claim page
            messages.info(request, _('Claim successfuly added'))
            return HttpResponseRedirect(reverse('claims.views.detail', args=(c.id, c.slug)))
    form = ClaimForm()
    return render_to_response('new.html', {'form': form}, context_instance=RequestContext(request))


def edit(request, id, slug):
    c = get_object_or_404(Claim, id=id)
    if request.method == 'POST':
        form = ClaimForm(request.POST, instance=c)
        if form.is_valid():
            c = form.save()
            messages.info(request, _('Claim successfuly edited'))
            return HttpResponseRedirect(reverse('claims.views.detail', args=(c.id, c.slug)))
        messages.info(request, _('Oops! Something happenned. Try again.'))
    
    form = ClaimForm(instance=c)
    data = {
        'form': form,
        'id': id,
    }
    return render_to_response('edit.html', data, context_instance=RequestContext(request))

   
def resolved(request):
    claimsResolved = Claim.objects.filter(resolved=True)
    data = {
        'claims': claimsResolved
    }
    return render_to_response('resolved.html', data, context_instance=RequestContext(request))