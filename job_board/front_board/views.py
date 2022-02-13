from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def demo():
    return JSONresponse({'1': 'test'})