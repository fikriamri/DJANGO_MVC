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
class Dokter(models.Model):
    nama = models.CharField(max_length=255)
    no_telp = models.CharField(max_length=17)
    bidang = models.CharField(max_length=255)
    hari_praktik = models.CharField(choices=DAYS,max_length=3)
    jam_praktik = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length=255)
    no_telp = models.CharField(max_length=17)
    alamat = models.TextField(max_length=255)
    keluhan = models.TextField(max_length=255)

    def __str__(self):
        return self.nama

class Resep(models.Model):
    nama = models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (dalam Rp.)")
    kumpulan_obat = models.TextField(max_length=255)

    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama = models.CharField(max_length=255)
    kandungan = models.CharField(max_length=255)
    khasiat = models.TextField(max_length=255)

    def __str__(self):
        return self.nama





