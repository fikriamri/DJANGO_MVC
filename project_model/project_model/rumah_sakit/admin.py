from django.contrib import admin
from .models import Dokter, Pasien, Resep, Obat

# Register your models here.
class DokterAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telp', 'bidang', 'hari_praktik', 'jam_praktik')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']
    
class PasienAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telp', 'alamat', 'keluhan')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

class ResepAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'price', 'kumpulan_obat')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

class ObatAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'kandungan', 'khasiat')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']


admin.site.register(Dokter, DokterAdmin)
admin.site.register(Pasien, PasienAdmin)
admin.site.register(Resep, ResepAdmin)
admin.site.register(Obat, ObatAdmin)

