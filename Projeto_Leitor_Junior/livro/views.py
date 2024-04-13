from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def  home(request):
    if request.get('usuario'):
        return HttpResponse('Homepage')
    else:
        return redirect('/auth/login/?status=2')