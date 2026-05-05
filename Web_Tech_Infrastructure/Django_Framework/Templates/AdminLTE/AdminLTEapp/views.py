from django.shortcuts import render
from django.http import Http404

# Create your views here.


def DashBoardOne(request):
    return render(request, "index1.html")


def DashBoardTwo(request):
    return render(request, "index2.html")


def DashBoardThree(request):
    return render(request, "index3.html")
