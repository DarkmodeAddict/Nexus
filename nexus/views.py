from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Nux
from .forms import NuxForm, SignUpForm, ProfilePicForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

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

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registered successfully! Welcome to Nexus.com!'))
            return redirect('home')
    return render(request, 'register.html', {'form':form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            login(request, current_user)
            messages.success(request, ('Your Profile has been updated!'))
            return redirect('home')
        return render(request, 'update_user.html', {'user_form':user_form, 'profile_form':profile_form})
    else:
        messages.success(request, ('You are not logged in'))
        return redirect('home')
    
def nex_like(request, pk):
    if request.user.is_authenticated:
        nex = get_object_or_404(Nux, id=pk)
        if nex.likes.filter(id=request.user.id):
            nex.likes.remove(request.user)
        else:
            nex.likes.add(request.user)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, ('You are not logged in!'))
        return redirect('home')
    
def nex_show(request, pk):
    nex = get_object_or_404(Nux, id=pk)
    if nex:
        return render(request, 'show_nex.html', {'nex':nex})
    else:
        messages.success(request, ('Nex not found!'))
        return redirect('home')
    
def unfollow(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        request.user.profile.follows.remove(profile)
        request.user.profile.save()
        messages.success(request, (f'Unfollowed {profile.user.username}'))
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, ('You are not logged in!'))
        return redirect('home')
    
def follow(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        request.user.profile.follows.add(profile)
        request.user.profile.save()
        messages.success(request, (f'Followed {profile.user.username}'))
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.success(request, ('You are not logged in!'))
        return redirect('home')
    
def followers(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)
            return render(request, 'followers.html', {'profiles': profiles})
        else:
            messages.success(request, ('That is not your profile'))
            return redirect('home')
    else:
        messages.success(request, ('You must be logged in to see others profiles'))
        return redirect('home')

def follows(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)
            return render(request, 'follows.html', {'profiles': profiles})
        else:
            messages.success(request, ('That is not your profile'))
            return redirect('home')
    else:
        messages.success(request, ('You must be logged in to see others profiles'))
        return redirect('home')