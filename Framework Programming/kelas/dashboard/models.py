from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    tipe_brg=models.CharField(max_length=50)
    jenis_id=models.ForeignKey(jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
       return "{} - {}".format(self.kodebrg,self.nama)

class Member(models.Model):
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    join_date=models.CharField(max_length=50)
    subscribe=models.CharField(max_length=50)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.email,self.username,self.status,self.join_date,self.subscribe)