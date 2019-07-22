from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import date
from django.utils import timezone

DAYS = (
            ('Mon','Monday'),
            ('Tue','Tuesday'),
            ('Wed','Wednesday'),
            ('Thu','Thursday'),
            ('Fri', 'Friday'),
            ('Sat', 'Saturday'),
            ('Sun', 'Sunday')
            )
            
# Create your models here.
class Penjaga(models.Model):
    nama = models.CharField(max_length=255)
    no_telp = models.CharField(max_length=17)
    jadwal_jaga = models.CharField(choices=DAYS,max_length=3)

    def __str__(self):
        return self.nama


class Pengunjung(models.Model):
    nama = models.CharField(max_length=255)
    no_telp = models.CharField(max_length=17)
    hari_berkunjung = models.DateField(auto_now=False)

    def __str__(self):
        return self.nama

class Hewan(models.Model):
    nama = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    berat = models.PositiveIntegerField(default=0, verbose_name='Berat (dalam kg)')
    umur = models.PositiveIntegerField(default=0, verbose_name='Umur (dalam tahun)')

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length=255)
    isi_kandang = models.TextField(max_length=255)
    luas_kandang = models.PositiveIntegerField(default=0, verbose_name='Luas Kandang (dalam m2)')

    def __str__(self):
        return self.nama