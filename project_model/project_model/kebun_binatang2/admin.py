from django.contrib import admin
from .models import Penjaga, Pengunjung, Hewan, Kandang

# Register your models here.

class PenjagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telp', 'jadwal_jaga')

class PengunjungAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telp', 'hari_berkunjung')

class HewanAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'species', 'berat', 'umur')

class KandangAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'isi_kandang', 'luas_kandang')

admin.site.register(Penjaga, PenjagaAdmin)
admin.site.register(Pengunjung, PengunjungAdmin)
admin.site.register(Hewan, HewanAdmin)
admin.site.register(Kandang, KandangAdmin)

