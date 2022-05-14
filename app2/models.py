from django.db import models
from django.utils import timezone

# Create your models here.

# Director クラス
class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="監督") # 監督名をnameフィールドに入れる
    
    def __str__(self):
        return self.name

# Movie クラス
class Movie(models.Model):
    title      = models.CharField(max_length=100, verbose_name="タイトル")
    watch_date = models.DateField()
    director   = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name="監督", related_name='movie') # Director表から紐付け
    
    def __str__(self):
        return self.title

# Log クラス
class Log(models.Model):
    text  = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="タイトル", related_name='log') # Movie表から紐付け
    
    def __str__(self):
        return self.text