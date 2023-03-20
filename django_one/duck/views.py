from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a form to create a new blog")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse("placeholder to to display blog number:{num}")

def edit(request, num):
    return HttpResponse("placeholder to to edit blog number:{num}")

def destroy(request, num):
    return redirect('/blogs')

def json(request):
    return JsonResponse({
                            "title": "My first blog",
                            "content": " Lorem ipsum dolor sit amet consectetur adipiscing elit.",
                            
                            
                        })
