# coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.template import RequestContext

from quejas.forms import QuejaForm

# Templates in Django need a "Context" to parse with, so we'll borrow this.
# "Context"'s are really nothing more than a generic dict wrapped up in a
# neat little function call.
from django.template import Context

from quejas.models import Queja
from usuarios.models import Usuario

def index(request):    
    quejasList = Queja.objects.order_by('votos')
    data = {
        'quejas': quejasList,
    }    
    return render_to_response('index.html', data, context_instance=RequestContext(request))
    
def detalle(request, id, slug):
    queja = get_object_or_404(Queja, id=id)
    
    data = {
        'queja': queja,
    }
    
    return render_to_response('quejas/detalle.html', data, context_instance=RequestContext(request))
    
def nueva(request):
    if request.method == 'POST':
        queja = QuejaForm(request.POST)
        if queja.is_valid():
                queja.save()
                #messages.add_message(request, messages.SUCCESS, message='Queja creada!')

                return HttpResponseRedirect('/')

    form = QuejaForm()

    return render_to_response('nueva.html', {'form': form}, context_instance=RequestContext(request))