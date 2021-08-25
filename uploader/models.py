from django.db import models
class Movies(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    about = models.TextField(max_length=1000) 
    link = models.TextField(max_length=1000)
    posterUrl = models.TextField(max_length=1000)
    c_posterUrl = models.TextField(max_length=1000)
    category = models.CharField(max_length=50)
    class Meta:
        db_table = 'movies'