from django.shortcuts import render

import authentication.views


# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # check db
        return render(request, 'core/index.html' )
    elif request.method == 'GET':
        return render(request, 'auth/login.html')

def reset_password(request):
    pass


