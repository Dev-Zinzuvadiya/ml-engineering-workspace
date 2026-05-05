from django.shortcuts import render, redirect

# Create your views here.


def FrontendPage(request):
    return render(request, "index.html")