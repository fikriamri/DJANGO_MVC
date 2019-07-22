from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import date
from django.utils import timezone

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telp = models.CharField(max_length=17)
    jabatan = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telp = models.CharField(max_length=17)
    nomor_absen = models.IntegerField()
    nilai_rata_rata = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.nama_lengkap


class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=255)
    jadwal_dimulai = models.DateField(auto_now=False)
    jadwal_berakhir = models.DateField(auto_now=False)

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telp = models.CharField(max_length=17)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal = models.PositiveIntegerField(default=0)
    bobot_nilai = models.PositiveIntegerField(default=0, verbose_name='Bobot nilai (dalam persen)')
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_challenge

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=255)
    banyak_soal = models.PositiveIntegerField(default=0)
    bobot_nilai = models.PositiveIntegerField(default=0, verbose_name='Bobot nilai (dalam persen)')
    tanggal_pelaksanaan = models.DateField(auto_now=False)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_live_code