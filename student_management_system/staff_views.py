from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


def HOME(request):
    return render(request,'Staff/home.html')
def take_attendance(request):

    return render(request, 'take_attendance.html')