from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import requests


@login_required(login_url='/auth_app/login/')
def home(request):
    name_user = request.user.social_auth.filter(provider='vk-oauth2')[0]
    if name_user:
        user_params = {
            'v': '5.92',
            'access_token': name_user.extra_data.get('access_token'),
            'count': '5',
            'order': 'random',
            'fields': ['photo_50']
        }
        response = requests.get('https://api.vk.com/method/friends.get', params=user_params).json()
        return render(request, 'auth_app/home.html', response)
    else:
        logout_vk(request)


def logout_vk(request):
    logout(request)
    return redirect('/auth_app/')


def login_vk(request):
    if request.user.is_authenticated:  # "if is_complete_authorization(request):" for several backends
        return redirect('/auth_app/')
    return render(request, 'auth_app/login.html')



