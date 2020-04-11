from django.shortcuts import render
from django.http import HttpResponse


def conversation_list(request):
    return HttpResponse("You're seeing all the conversations you have!")
    
