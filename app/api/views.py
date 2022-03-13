from urllib import response
from django.shortcuts import redirect, render

def StableApiVersion(request):
    response = redirect('/api/v0.0.1/')
    return response