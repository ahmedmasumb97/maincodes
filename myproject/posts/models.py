from django.db import models
from authors.models import Author
from categories.models import Catagory

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


    Catagory = models.ManyToManyField(Catagory)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    