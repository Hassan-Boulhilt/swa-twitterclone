from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Twitte

@login_required
def feed(request):
   userids = [request.user.id]

   for twitter in request.user.twitterprofile.follows.all():
      userids.append(twitter.user.id)

   twittes =Twitte.objects.filter(created_by_id__in=userids)
   return render(request,'feed/feed.html', {'twittes': twittes})

@login_required
def search(request):
   query = request.GET.get('query','')

   if len(query) > 0:
      twitters = User.objects.filter(username__icontains = query)
   else:
      twitters = []
   context = {
      'query': query,
      'twitters': twitters
   }
   return render(request, 'feed/search.html', context)
