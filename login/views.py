from email import message
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
def user_login (request):
    if 'username' in request.session:
        return redirect(home)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            request.session['username'] = username
            return redirect(home)
        else:
            messages.error(request, 'Invalid Credintials!!!')
            return redirect(user_login)
    return render (request, 'index.html')
@never_cache
def home(request):
    if 'username' in request.session:
        return render(request, 'home.html')
    return redirect(user_login)

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(user_login)
    
