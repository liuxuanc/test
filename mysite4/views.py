from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'toot.html')
def book(request):
    return HttpResponse('图书')

# def book_detail(request,book_id):
#     text = '您的书记图书id为%s'% book_id
#     return HttpResponse(text)

def movie(request):
    return HttpResponse('电影')
def tongc(request):
    return HttpResponse('同城')