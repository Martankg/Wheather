from django.db import models

# Create your models here.
class SearchedCity(models.Model):
    city=models.CharField(max_length=50, verbose_name='City')
    temperature=models.IntegerField(verbose_name='Temperature')
    sent_at=models.DateTimeField(auto_now_add=True, verbose_name='Date and time')
    updated=models.DateTimeField(auto_now=True, verbose_name='Update time')
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.city