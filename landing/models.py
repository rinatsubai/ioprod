from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=512)
    picture = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
    
class Artist(models.Model):
    name = models.CharField(max_length=512)
    genre = models.ManyToManyField(Genre)
    description = models.CharField(max_length=512)
    picture = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
    
class Release(models.Model):
    name = models.CharField(max_length=512)
    date = models.CharField(max_length=512)
    picture = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=512)
    link = models.CharField(max_length=512)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="release_set")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-date"]
    