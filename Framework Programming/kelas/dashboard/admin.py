from django.contrib import admin

# Register your models here.
from .models import Barang,jenis,Member

class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg','nama','stok','harga','tipe_brg']
    search_fields = ['kodebrg','nama']

class kolomMember(admin.ModelAdmin):
    list_display = ['email','username','status','join_date']
    search_fields = ['kodebrg','nama']

admin.site.register(Barang,kolomBarang)
admin.site.register(jenis) 
admin.site.register(Member,kolomMember)