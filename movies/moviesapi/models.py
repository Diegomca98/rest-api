from django.db import models

# Create your models here.
class MovieData(models.Model):
    name = models.CharField(max_length=200, verbose_name="Movie")
    duration = models.FloatField(verbose_name="Duration")
    rating = models.FloatField(verbose_name="Rating")
    category = models.CharField(max_length=200, default="action")
    image = models.ImageField(upload_to='images/', default='images/None/Noimg.jpg')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"