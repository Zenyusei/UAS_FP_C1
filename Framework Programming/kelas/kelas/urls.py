"""kelas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from __future__ import absolute_import
from django.contrib import admin
from django.urls import path

from dashboard.views import Barang_View, item, store, tambah_barang , about, daftar, login, Member_View, tambah_member
from dashboard.views import pay


from django.http import HttpResponse
from dashboard.views import *

def coba1(request):
    return HttpResponse('Selamat datang')


from django.shortcuts import render
def coba2(request):
    titlenya="Home"
    konteks = {
        'title':titlenya,
    }
    return render(request,'index.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',coba2),
    path('store/',store),
    path('pay/', pay),
    path('addbrg/',tambah_barang),
    path('addmbr/',tambah_member),
    path('dftr/',Barang_View, name='dftr'),
    path('item/',item),
    path('about/', about),
    path('daftar/', daftar),
    path('login/', login),
    path('member/', Member_View, name='member'),
    path('ubah/<int:id_barang>', ubah_brg , name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg, name='hapus_brg'),
    path('ubahm/<int:id_member>', ubah_mbr , name='ubah_mbr'),
    path('hapusm/<int:id_member>',hapus_mbr, name='hapus_mbr'),
]
