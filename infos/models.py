#from turtle import title
from django.db import models

# Create your models here.


class Dergiler(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik", default="Default")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturma Tarihi"
    )
    dergi_kapak = models.FileField(default="Default", verbose_name="Dergi Kapak")
    dergi_pdf = models.FileField(default="Default", verbose_name="Dergi Dosya Pdf")

    def __str__(self):
        return self.title


class Yazarlar(models.Model):
    isim = models.CharField(max_length=100, verbose_name="İsim", default="İsim Gir")
    gorev = models.TextField(verbose_name="Görevi", default="Default")

    def __str__(self):
        return self.isim


class Slider(models.Model):
    isim = models.CharField(
        max_length=100,
        verbose_name="İsim",
        default="Minimum en az iki tane slider girin",
    )
    slider_image = models.FileField(
        blank=True, null=True, default="Default", verbose_name="Resim Ekle"
    )

    slider_link= models.CharField(
        max_length=1000,
        verbose_name="verilecek linki çift tırnak içinde yazın",
        default="link girin",
    )

    def __str__(self):
        return self.isim


class Small_Slider(models.Model):
    isim = models.CharField(
        max_length=100,
        verbose_name="İsim",
        default="Minimum en az iki tane slider girin",
    )
    slider_image = models.FileField(
        blank=True, null=True, default="Default", verbose_name="Küçük Resim Ekle"
    )

    def __str__(self):
        return self.isim


class Hakkimizda(models.Model):
    title = models.CharField(max_length=150, verbose_name="İsim", default="Başlık Gir")
    contents = models.TextField(verbose_name="Görevi", default="İçerik")
    image = models.FileField(
        blank=True, null=True, default="Default", verbose_name="Hakkımızda Resim"
    )

    def __str__(self):
        return self.title



class Renkler(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Aga bundan bir tane oluşturacaksınız",
        default="Aga bundan bir tane oluşturacaksınız",
    )
    font = models.TextField(
        verbose_name="Title Font", default="Arial, Helvetica, sans-serif"
    )
    Navbar = models.TextField(verbose_name="Navbar Renk", default="rgb(141, 173, 222)")
    Hakkimizda = models.TextField(
        verbose_name="Hakkımızda Renk", default="rgb(163, 239, 239)"
    )
    Slider_arka_plan = models.TextField(
        verbose_name="Slider_arka_plan Renk", default="#E2F4E0"
    )
    Sayılar = models.TextField(
        verbose_name="Sayılar Renk", default="rgb(192, 219, 127)"
    )
    Yazarlar = models.TextField(verbose_name="Yazarlar Renk", default="cadetblue")
    copyright = models.TextField(verbose_name="copyright Renk", default="#1a252f")

    def __str__(self):
        return self.title
        



class Logo(models.Model):
    isim = models.CharField(
        max_length=100,
        verbose_name="İsim",
        default="Logo Giriniz: ",
    )
    logo_image = models.FileField(
        blank=True, null=True, default="Default", verbose_name="Resim Ekle"
    )

    def __str__(self):
        return self.isim
