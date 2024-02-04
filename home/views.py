from django.shortcuts import render, redirect

from django.http import HttpResponse
# from .utils import send_email_to_client

# def send_email(request):
#     send_email_to_client()
#     return redirect('/')

def home(request):

    peoples = [
        {'name':'Abhijit Sharma', 'age':55},
        {'name':'Chetan Darji', 'age':45},
        {'name':'Ankit Malvi', 'age':35},
        {'name':'Dhirz Malvi', 'age':25},
        {'name':'Prem Malvi', 'age':15},
    ]

    vegatables = ['Pumpkin', 'Tomato', 'Potatoe']


    return render(request, "index.html", context= {'page':'Django Testing', 'peoples':peoples, 'vegatables':vegatables})

def contact(request):
    context = {'page':'Contact'}
    return render(request, "contact.html", context)

def about(request):
    context = {'page':'About'}
    return render(request, "about.html", context)

def success_page(request):
    return HttpResponse("<h1>Hey, I'm a Success Page</h1>")