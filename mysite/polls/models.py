from django.db import models

class Sorular(models.Model):
    soru_metni=models.CharField(max_length=200)
    tarih     =models.DateTimeField('tarihi')
class Secim(models.Model):
    soru    =models.ForeignKey(Sorular, on_delete=models.CASCADE)
    secim_metni = models.CharField(max_length=200)
    oylar  =models.IntegerField(default=0)
# Create your models here.
