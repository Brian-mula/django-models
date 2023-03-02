from django.db import models

# Create your models here.

class Blogs(models.Model):
    creater=models.CharField(max_length=50,default="Mulati brian")
    title=models.CharField(max_length=50)
    description=models.TextField()
    created_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.creater

class MenuCategory(models.Model):
    category_name=models.CharField(max_length=200)

class Menu(models.Model):
    menu_item=models.CharField(max_length=200)
    price=models.IntegerField(null=False)
    category_id=models.ForeignKey(MenuCategory,on_delete=models.PROTECT)