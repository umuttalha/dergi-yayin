# Generated by Django 4.0 on 2022-08-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dergiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('content', models.TextField(default='Default', verbose_name='İçerik')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')),
                ('dergi_kapak', models.FileField(default='Default', upload_to='', verbose_name='Dosya Ekle')),
                ('dergi_pdf', models.FileField(default='Default', upload_to='', verbose_name='Dosya Ekle')),
            ],
        ),
        migrations.CreateModel(
            name='Hakkımızda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Başlık Gir', max_length=150, verbose_name='İsim')),
                ('contents', models.TextField(default='İçerik', verbose_name='Görevi')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(default='İsim Gir', max_length=100, verbose_name='İsim')),
                ('slider_image', models.FileField(blank=True, default='Default', null=True, upload_to='', verbose_name='Resim Ekle')),
            ],
        ),
        migrations.CreateModel(
            name='Yazarlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(default='İsim Gir', max_length=100, verbose_name='İsim')),
                ('gorev', models.TextField(default='Default', verbose_name='Görevi')),
            ],
        ),
    ]