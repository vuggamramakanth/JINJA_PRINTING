from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jinja_print(requset):
    d={'name':'RAMAKANTH YADAV','age':24}
    return render(requset,'jinja_print.html',d)