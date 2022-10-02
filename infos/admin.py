from django.contrib import admin

from .models import Dergiler ,Logo , Small_Slider, Yazarlar, Slider, Hakkimizda, Renkler

# Register your models here.


@admin.register(Logo)
class InfoAdmin(admin.ModelAdmin):
    list_display = ["isim"]
    list_display_links = ["isim"]
    search_fields = ["isim"]

    class Meta:
        model = Logo


@admin.register(Dergiler)
class InfoAdmin(admin.ModelAdmin):

    list_display = ["title", "created_date"]
    list_display_links = ["title"]
    search_fields = ["title"]
    list_filter = ["created_date"]

    class Meta:
        model = Dergiler


@admin.register(Yazarlar)
class InfoAdmin(admin.ModelAdmin):

    list_display = ["isim"]
    list_display_links = ["isim"]
    search_fields = ["gorev"]

    class Meta:
        model = Yazarlar


@admin.register(Slider)
class InfoAdmin(admin.ModelAdmin):

    list_display = ["isim"]
    list_display_links = ["isim"]
    search_fields = ["isim"]

    class Meta:
        model = Slider


@admin.register(Small_Slider)
class InfoAdmin(admin.ModelAdmin):

    list_display = ["isim"]
    list_display_links = ["isim"]
    search_fields = ["isim"]

    class Meta:
        model = Small_Slider


@admin.register(Hakkimizda)
class InfoAdmin(admin.ModelAdmin):

    list_display = ["title"]
    list_display_links = ["title"]
    search_fields = ["title"]

    class Meta:
        model = Hakkimizda


@admin.register(Renkler)
class InfoAdmin(admin.ModelAdmin):

    list_display = ["title"]
    list_display_links = ["title"]
    search_fields = ["title"]

    class Meta:
        model = Renkler

