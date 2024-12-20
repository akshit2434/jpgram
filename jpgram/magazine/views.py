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
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title":"CICE", "title": "CICE Gallery"}
    )


def crescendojiit(request):
    club = "crescendojiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title":"Crescendo", "title": "Crescendo Gallery"}
    )


def dscjiit(request):
    club = "dscjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title":"DSC", "title": "DSC Gallery"}
    )


def jaypee_photo_enthusiasts_guild(request):
    club = "jaypee.photo.enthusiasts.guild"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title":"JPEG", "title": "JPEG Gallery"}
    )


def jhankaarjiit(request):
    club = "jhankaarjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "Jhankaar", "title": "Jhankaar Gallery"}
    )


def jiit_impressions(request):
    club = "jiit.impressions"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "JIIT Impressions", "title": "JIIT Impressions Gallery"}
    )


def jiityouthclub(request):
    club = "jiityouthclub"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "JIIT Youth Club", "title": "JIIT Youth Club Gallery"}
    )


def knuth_jiit(request):
    club = "knuth_jiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "Knuth", "title": "Knuth Gallery"}
    )


def nssjiit62(request):
    club = "nssjiit62"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "NSS", "title": "NSS Gallery"}
    )


def osdcjiit(request):
    club = "osdcjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "OSDC", "title": "OSDC Gallery"}
    )


def parola_literaryhub(request):
    club = "parola.literaryhub"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "Parola Literary Hub", "title": "Parola Literary Hub Gallery"}
    )


def radiance_hub(request):
    club = "radiance.hub"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "Radiance Hub", "title": "Radiance Hub Gallery"}
    )


def thejaypeedebsoc(request):
    club = "thejaypeedebsoc"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "Jaypee Debsoc", "title": "Jaypee Debsoc Gallery"}
    )


def thepageturnersociety(request):
    club = "thepageturnersociety"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "The Page Turner Society", "title": "The Page Turner Society Gallery"}
    )


def thethespiancircle(request):
    club = "thethespiancircle"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "Thespian Circle", "title": "Thespian Circle Gallery"}
    )


def ucrjiit(request):
    club = "ucrjiit"
    image_index = cache.get("image_index")

    if not image_index:
        image_index = fetch_index()
        cache.set("image_index", image_index, timeout=3600)
    image_index = fetch_index()

    return render(
        request, f"magazine/{club}.html", {"image_data_list": image_index[club], "page_title": "UCR", "title": "UCR Gallery"}
    )
