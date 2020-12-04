from django.shortcuts import render

def frontpage(request):
    render(request,'core/frontpage.html',)