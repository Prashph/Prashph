from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('this is index page') 


def testtoshow(request):
    return HttpResponse('this is test page')