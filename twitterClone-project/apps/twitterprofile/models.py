from django.contrib.auth.models import User
from django.db import models


class TwitterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
User.twitterprofile = property(lambda u: TwitterProfile.objects.get_or_create(user=u)[0])