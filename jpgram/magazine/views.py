from django.shortcuts import render
from django.core.cache import cache
from .models import fetch_index


def index(request):
    return render(request, "base.html")


def cice_jiit(request):
    club = "cice_jiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"CICE JIIT",
            "page_title": "CICE"
        }
    )



def crescendojiit(request):
    club = "crescendojiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        logger.debug("Fetched Index: %s", image_index)  # Logging
        cache.set("image_index", image_index, timeout=3600)

    image_data_list = image_index.get(club, [])
    logger.debug("Image Data List for %s: %s", club, image_data_list)  # Logging

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"Crescendo JIIT",
            "page_title": "Crescendo"
        }
    )


def gdscjiit(request):
    club = "gdscjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    
    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"GDSC JIIT",
            "page_title": "GDSC"
        }
    )


def jaypee_photo_enthusiasts_guild(request):
    club = "jaypee.photo.enthusiasts.guild"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"JPEG JIIT",
            "page_title": "JPEG"
        }
    )


def jhankaarjiit(request):
    club = "jhankaarjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"Jhankaar JIIT",
            "page_title": "Jhankaar"
        }
    )


def jiit_impressions(request):
    club = "jiit.impressions"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"Impressions JIIT",
            "page_title": "Impressions"
        }
    )


def jiityouthclub(request):
    club = "jiityouthclub"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"JYC JIIT",
            "page_title": "JYC"
        }
    )


def knuth_jiit(request):
    club = "knuth_jiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"Knuth JIIT",
            "page_title": "Knuth"
        }
    )


def nssjiit62(request):
    club = "nssjiit62"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"NSS JIIT",
            "page_title": "NSS"
        }
    )


def osdcjiit(request):
    club = "osdcjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"OSDC JIIT",
            "page_title": "OSDC"
        }
    )


def parola_literaryhub(request):
    club = "parola.literaryhub"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"Parola JIIT",
            "page_title": "Parola"
        }
    )


def radiance_hub(request):
    club = "radiance.hub"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"Radiance JIIT",
            "page_title": "Radiance"
        }
    )


def thejaypeedebsoc(request):
    club = "thejaypeedebsoc"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"Debsoc JIIT",
            "page_title": "Debsoc"
        }
    )


def thepageturnersociety(request):
    club = "thepageturnersociety"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"Page Turner JIIT",
            "page_title": "Page Turner"
        }
    )


def thethespiancircle(request):
    club = "thethespiancircle"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"Thespian Circle JIIT",
            "page_title": "Thespian Circle"
        }
    )


def ucrjiit(request):
    club = "ucrjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)

    return render(
        request, f"magazine/gallery_template.html", {
            "image_data_list": image_index[club], 
            "title":"μCR JIIT",
            "page_title": "μCR"
        }
    )
