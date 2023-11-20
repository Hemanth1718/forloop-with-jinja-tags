from django.shortcuts import render

# Create your views here.

d={'name':'HEMANTH'}
def forloop(request):
    return render(request,'forloop.html',d)
