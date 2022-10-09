from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

from App_Login.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import messages

def sign_up(request):

    form = SignUpForm()

    if request.method == 'POST':

        form = SignUpForm(data=request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, 'Account created successfully!')

            return HttpResponseRedirect(reverse('App_Login:login'))



    dict = {'title' : 'Sign Up', 'form' : form}

    return render(request, 'App_Login/sign_up.html', context=dict)


def user_login(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)

                messages.success(request, 'Successfully login to the home page!')

                return HttpResponseRedirect(reverse('App_Login:home'))

    dict = {'title' : 'Login', 'form' : form}

    return render(request, 'App_Login/login.html', context=dict)


 
def home(request):

    if request.user.is_authenticated:

        dict = {'title' : 'Home'}
        return render(request, 'App_Login/home.html', context=dict)

    else:

        return HttpResponseRedirect(reverse('App_Login:login'))

@login_required
def user_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('App_Login:login'))
    
