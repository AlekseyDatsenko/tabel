from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    #self.the_class = models.ForeignKey(TheClass, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return (self.last_name + ' ' + self.first_name)




   
