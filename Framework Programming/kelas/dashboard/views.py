from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from dashboard.forms import FormBarang
from dashboard.forms import FormMember
from dashboard.models import Barang
from dashboard.models import Member
from django.contrib import messages

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def Member_View(request):
    members=Member.objects.all()

    konteks={
        'members':members,
    }
    return render(request,'member.html',konteks)

def tambah_barang(request):
    if request.POST:
        form= FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form' : form,
            }
            return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)

def tambah_member(request):
    if request.POST:
        formm= FormMember(request.POST)
        if formm.is_valid():
            formm.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            formm = FormMember()
            konteks = {
                'formm' : formm,
            }
            return render(request,'tambah_member.html',konteks)
    else:
        formm=FormMember()
        konteks = {
            'formm':formm,
        }
    return render(request,'tambah_member.html',konteks)

def store(request):
    titlenya="store"
    konteks = {
        'title':titlenya,
    }
    return render(request,'store.html',konteks
    )

def pay(request):
    titlenya="pay"
    konteks = {
        'title':titlenya,
    }
    return render(request,'pay.html',konteks
    )

def item(request):
    titlenya="item"
    konteks = {
        'title':titlenya,
    }
    return render(request,'item.html',konteks
    )

def about(request):
    titlenya="about"
    konteks = {
        'title':titlenya,
    }
    return render(request,'about.html',konteks
    )

def daftar(request):
    titlenya="daftar"
    konteks = {
        'title':titlenya,
    }
    return render(request,'daftar.html',konteks
    )

def login(request):
    titlenya="login"
    konteks = {
        'title':titlenya,
    }
    return render(request,'login.html',konteks
    )

def member(request):
    titlenya="member"
    konteks = {
        'title':titlenya,
    }
    return render(request,'member.html',konteks
    )

def ubah_brg(request, id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form= FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

def ubah_mbr(request, id_member):
    members=Member.objects.get(id=id_member)
    if request.POST:
        formm= FormMember(request.POST,instance=members)
        if formm.is_valid():
            formm.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_mbr',id_member=id_member)
    else:
        formm=FormMember(instance=members)
        konteks = {
            'formm':formm,
            'members':members
        }
    return render(request,'ubah_mbr.html',konteks)

def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")
    return redirect('dftr')

def hapus_mbr(request,id_member):
    members=Member.objects.filter(id=id_member)
    members.delete()
    messages.success(request,"Data Terhapus")
    return redirect('member')