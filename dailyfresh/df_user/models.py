from django.db import models

# Create your models here.
class UserInfo(models.MOdel):
    uname = models.CharField(max_length=20)
    upwd = models.charField(max_length=40)
    
    def __str__(self):
        return "%d" %self.pk
