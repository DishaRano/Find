from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
'''class Interests(models.Model):
    name = models.CharField(max_length=30)
    interes = models.CharField(max_length=40)


    class Meta:
      verbose_name_plural = "interest"

    def __str__(self):
        return self.name'''



class Item(models.Model):
    video = EmbedVideoField()
    name = models.CharField(max_length=300)