from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def feed(request):
   return render(request,'feed/feed.html')