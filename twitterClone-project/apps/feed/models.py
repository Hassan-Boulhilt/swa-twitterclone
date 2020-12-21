from django.db import models

from django.contrib.auth.models import User

<<<<<<< HEAD

class Twitte(models.Model):
    body = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='twitte',on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
=======
class Twitt(models.Model):
    body = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='twitts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

>>>>>>> 48c93aae2aff1d0a400f289eb6576471f1be919b

    class Meta:
        ordering = ('-created_at',)
