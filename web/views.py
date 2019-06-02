from django.shortcuts import render, redirect
from web import models
# Create your views here.


def index(request):
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"user_list": user_list})


def add(request):
    models.UserInfo.objects.create(
        name='song',
        pwd='123',
    )
    return redirect('/index/')


def remove(request):
    models.UserInfo.objects.filter(pwd='123456').delete()
    return redirect('/index/')


def update(request):
    models.UserInfo.objects.all().update(pwd='123456')
    return redirect('/index/')
