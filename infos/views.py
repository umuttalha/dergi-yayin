from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Dergiler,Logo, Slider, Yazarlar, Hakkimizda, Small_Slider, Renkler

def index(request):

    sliders = Slider.objects.all()
    slider_active = sliders[0]
    sm_sliders = Small_Slider.objects.all()
    sm_slider_active = sm_sliders[0]

    sm_sliders = list(sm_sliders)
    sm_sliders.pop(0)

    sliders = list(sliders)
    sliders.pop(0)

    renkler = Renkler.objects.all()
    about = Hakkimizda.objects.all()
    sayilar = Dergiler.objects.all()
    # yazarlar = Yazarlar.objects.all()

    logo = Logo.objects.all()[0]


    context = {
        "renkler": renkler[0],
        "sliders": sliders,
        "slider_active": slider_active,
        "about": about,
        "sayilar": sayilar,
        # "yazarlar": yazarlar,
        "sm_slider_active": sm_slider_active,
        "sm_sliders": sm_sliders,
        "logo": logo,
    }
    return render(request, "index.html", context)


def detail(request,id):
    renkler = Renkler.objects.all()
    logo = Logo.objects.all()[0]
    dergi = get_object_or_404(Dergiler,id=id)
    context={
        "renkler": renkler[0],
        "dergi":dergi,
        "logo": logo,
    }
    return render(request,"detail.html",context)

def yazarlar(request):
    yazarlar = Yazarlar.objects.all()
    logo = Logo.objects.all()[0]
    renkler = Renkler.objects.all()
    context={
        "renkler": renkler[0],
        "yazarlar":yazarlar,
        "logo": logo,
    }
    return render(request,"yazarlar.html",context)