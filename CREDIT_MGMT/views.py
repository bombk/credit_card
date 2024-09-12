from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    if user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If the user exists and the credentials are correct, log the user in
            auth_login(request, user)
            return redirect('home')
        else:
            # If the authentication fails, send an error response
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password'})
    else:
        def get(self, request, *args, **kwargs):
            if request.user.is_authenticated:
                # Redirect to the homepage or another page if the user is already logged in
                return redirect('home')  # Replace 'home' with the name of your desired redirect URL
            return super().get(request, *args, **kwargs)
        return render(request, 'authentication/login.html')
    
def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to the login page after logout