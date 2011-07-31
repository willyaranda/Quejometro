from django.http import HttpResponseRedirect

from accounts.utils import createUser

def profile(request):
    return HttpResponseRedirect("/")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #createUser
            #TODO: redirect to the user profile page
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {'form': form,})