from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views



from apps.core.views import frontpage, signup
from apps.feed.views import feed, search
from apps.twitterprofile.views import twitterprofile

from apps.feed.api import api_add_twitte






 

urlpatterns = [
    #
    #

    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    
    
    path('feed/', feed, name='feed'),
    path('search/', search, name='search'),
    path('u/<str:username>/',twitterprofile, name='twitterprofile'),



    #
    # API urls

    path('api/add_twitte/',api_add_twitte, name='api_add_twitte'),

    #
    # Admin

    path('admin/', admin.site.urls),
    
    ]