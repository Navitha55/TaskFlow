from django.shortcuts import render
from django.http import JsonResponse

def index_page(req):
    return render(req,'index.html')
