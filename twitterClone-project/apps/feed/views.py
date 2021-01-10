from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Twitte

@login_required
def feed(request):
   userids = [request.user.id]

   for twitter in request.user.twitterprofile.follows.all():
      userids.append(twitter.user.id)

   twittes =Twitte.objects.filter(created_by_id__in=userids)
   return render(request,'feed/feed.html', {'twittes': twittes})