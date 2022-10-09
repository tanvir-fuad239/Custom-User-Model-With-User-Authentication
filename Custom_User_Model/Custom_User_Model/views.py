from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

def index(request):

    return HttpResponseRedirect(reverse('App_Login:login'))

def main_home(request):

    return HttpResponseRedirect(reverse('App_Login:login'))