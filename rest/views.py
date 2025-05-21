from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#create your views here.

@login_required
def dashboard(request):   #Main screen
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})
