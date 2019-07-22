from django.contrib import admin
from .models import Dokter, Pasien, Resep, Obat

# Register your models here.
class DokterAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telp', 'bidang', 'hari_praktik', 'jam_praktik')

class PasienAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telp', 'alamat', 'keluhan')

class ResepAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'price', 'kumpulan_obat')

class ObatAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'kandungan', 'khasiat')


admin.site.register(Dokter, DokterAdmin)
admin.site.register(Pasien, PasienAdmin)
admin.site.register(Resep, ResepAdmin)
admin.site.register(Obat, ObatAdmin)

