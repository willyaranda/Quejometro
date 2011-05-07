#
#       Link between django and apache
#
import os, sys 

apache_configuration= os.path.dirname(__file__) 
project = os.path.dirname(apache_configuration) 
workspace = os.path.dirname(project) 

sys.path.append(workspace)

#The route of django module instalation
sys.path.append('/usr/lib/pymodules/python2.6/django/') 

#The route to the project dir
sys.path.append('/var/lib/mozevents/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Quejometro.settings' 

import django.core.handlers.wsgi 

application = django.core.handlers.wsgi.WSGIHandler()