from django.shortcuts import render,render_to_response
from django.template import Context, Template

#项目

def index(res):
    return render_to_response("index.html")