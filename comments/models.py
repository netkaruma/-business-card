from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from users.models import CustomUser
# Create your models here.
# from users.models import CustomUser

class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    likes = models.DecimalField(max_digits=100, decimal_places=0, default=0)
    value = models.CharField(null=True)


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # кто поставил лайк
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)  # на какой комментарий поставлен лайк
    date = models.DateTimeField(default=timezone.now)  # когда был поставлен лайк