from django.contrib import admin
from .models import MataPelajaran, Direksi, Mentee, Mentor, Challenge, LiveCode

# Register your models here.
class DireksiAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_lengkap', 'no_telp', 'jabatan')

class MenteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_lengkap', 'no_telp', 'nomor_absen', 'nilai_rata_rata')

class MataPelajaranAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_pelajaran', 'jadwal_dimulai', 'jadwal_berakhir')

class MentorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_lengkap', 'no_telp', 'mata_pelajaran')

class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_challenge', 'banyak_soal', 'bobot_nilai', 'mata_pelajaran')

class LiveCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_live_code', 'banyak_soal', 'bobot_nilai', 'tanggal_pelaksanaan', 'mata_pelajaran')


admin.site.register(MataPelajaran, MataPelajaranAdmin)
admin.site.register(Direksi, DireksiAdmin)
admin.site.register(Mentee, MenteeAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(LiveCode, LiveCodeAdmin)