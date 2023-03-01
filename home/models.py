from django.db import models

# Create your models here.

class Blogs(models.Model):
    creater=models.CharField(max_length=50,default="Mulati brian")
    title=models.CharField(max_length=50)
    description=models.TextField()
    created_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.creater