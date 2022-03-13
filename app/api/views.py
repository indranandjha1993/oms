from urllib import response
from django.shortcuts import redirect, render


def StableApiVersion(request):
    return redirect('/api/v0.0.1/')
