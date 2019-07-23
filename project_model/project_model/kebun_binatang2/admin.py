from django.contrib import admin
from .models import Penjaga, Pengunjung, Hewan, Kandang

# Register your models here.

class PenjagaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telp', 'jadwal_jaga')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

class PengunjungAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'no_telp', 'hari_berkunjung')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

class HewanAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'species', 'berat', 'umur')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

class KandangAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'isi_kandang', 'luas_kandang')
    list_display_links = ('id', 'nama')
    search_fields = ['nama']

admin.site.register(Penjaga, PenjagaAdmin)
admin.site.register(Pengunjung, PengunjungAdmin)
admin.site.register(Hewan, HewanAdmin)
admin.site.register(Kandang, KandangAdmin)

