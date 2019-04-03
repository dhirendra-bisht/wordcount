from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"home.html")

def count(request):
    data = request.GET['fulltextarea']
    word_list=data.split()
    total=len(word_list)
    print(word_list)
    print(total)
    return render(request,"count.html", {'fulltext' : data, 'tword':total})