from django.shortcuts import render

# Create your views here.


def frontend(re):
    return render(re, "index.html")
