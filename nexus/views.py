from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Nux
from .forms import NuxForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    if request.user.is_authenticated:
        form = NuxForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                nex = form.save(commit=False)
                nex.user = request.user
                nex.save()
                messages.success(request, ('Nexed'))
                return redirect('home')
        nux = Nux.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'nux': nux, 'form':form})
    else:
        nux = Nux.objects.all().order_by('-created_at')
        return render(request, 'home.html', {'nux': nux})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {'profiles': profiles})
    else:
        messages.success(request, ('You must be logged in to see others profiles'))
        return redirect('home')
    
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        nux = Nux.objects.filter(user_id=pk).order_by('-created_at')
        if request.method == 'POST':
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            current_user_profile.save()
        return render(request, 'profile.html', {'profile': profile, 'nux': nux})
    else:
        messages.success(request, ('You must be logged in to see others profiles'))
        return redirect('home')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in'))
            return redirect('home')
        else:
            messages.success(request, ('There was an error logging in'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('home')