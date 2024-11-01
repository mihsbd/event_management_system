from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, SignInForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Account Created Successfully!')
            return redirect('signin')
    else:
        form = SignUpForm()

    context = {'form': form, 'title': 'Sign Up'}
    return render(request, 'app_user/signup.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password!')
    else:
        form = SignInForm()
   
    context = {'form': form, 'title': 'Sign In'}
    return render(request, 'app_user/signin.html', context)


@login_required
def signout(request):
    logout(request)
    return redirect('home')


# Profile Views:
@login_required
def profile_view(request):
    profile = request.user.profile
    context = {'profile': profile, 'title': 'Profile'}
    return render(request, 'app_user/profile.html', context)


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'user_form': user_form, 'profile_form': profile_form, 'title': 'Profile Update'}
    return render(request, 'app_user/profile_update.html', context)