# Generated by Django 4.1 on 2022-08-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("infos", "0005_remove_renkler_contents_renkler_hakkımızda_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="renkler",
            name="Hakkımızda",
            field=models.TextField(
                default="rgb(163, 239, 239)", verbose_name="Hakkımızda Renk"
            ),
        ),
        migrations.AlterField(
            model_name="renkler",
            name="Navbar",
            field=models.TextField(
                default="rgb(141, 173, 222)", verbose_name="Navbar Renk"
            ),
        ),
        migrations.AlterField(
            model_name="renkler",
            name="Sayılar",
            field=models.TextField(
                default="rgb(192, 219, 127)", verbose_name="Sayılar Renk"
            ),
        ),
        migrations.AlterField(
            model_name="renkler",
            name="Yazarlar",
            field=models.TextField(default="cadetblue", verbose_name="Yazarlar Renk"),
        ),
        migrations.AlterField(
            model_name="renkler",
            name="copyright",
            field=models.TextField(default="#1a252f", verbose_name="copyright Renk"),
        ),
    ]
