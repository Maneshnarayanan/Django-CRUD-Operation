from django.shortcuts import render
from django.http import HttpResponse

def sample_msg(request):
    return HttpResponse("hii python django")

# def index(request):
#     return render(request, 'index.html')


def new_page(request):
    return render(request,'index.html')