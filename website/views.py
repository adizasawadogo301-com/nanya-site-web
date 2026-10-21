from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .data import DOMAINS, SERVICES
from .models import ContactMessage, ServiceRequest


def home(request):
    return render(request, "website/home.html", {"domains": DOMAINS})


def about(request):
    return render(request, "website/about.html")


def domains(request):
    return render(request, "website/domains.html", {"domains": DOMAINS})


def domain_detail(request, slug):
    domain = next((item for item in DOMAINS if item["slug"] == slug), None)
    if domain is None:
        raise Http404

    return render(request, "website/domain.html", {"domain": domain})


def services(request):
    return render(request, "website/services.html", {"services": SERVICES})


def partners(request):
    partners = [
        {"name": "Sonacom", "logo":
         None},
        {"name": "SUNU Bank", "logo":
         None},
        {"name": "GIZ", "logo":
         None},
        {"name": "STEEL CUBE", "logo": 
         None},
        {"name": "WAPAC", "logo":
         None},
        {"name": "MANUMETAL", "logo": 
         None},
        {"name": "Solo Tomate", "logo":
         None},
        {"name": "HYDRO LUB Sa", "logo":
         None},
        {"name": "MGTM (MEGA)", "logo":
         None},
        {"name": "A-Finances (Finance,Gestion & Stratégie)", "logo": 
         None},
        {"name": "TOROMETAL", "logo": 
         None},
        {"name": "FLEXIMETAL", "logo": 
         None},
        {"name": "BIZO-HEALTH", "logo":
         None},
        {"name": "LK", "logo":
         None},
        {"name": "GS (Voyage)", "logo": 
         None},
        {"name": "SOLIM (LOME-KARA-LOME)", "logo":
         None},
    ]
    return render(request, "website/partners.html", {"partners": partners})


def realizations(request):
    return render(request, "website/realizations.html")


def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name", ""),
            email=request.POST.get("email", ""),
            phone=request.POST.get("phone", ""),
            subject=request.POST.get("subject", ""),
            message=request.POST.get("message", ""),
        )
        messages.success(request, "Votre message a bien été enregistré.")
        return redirect("contact")

    return render(request, "website/contact.html")


def service_request(request):
    if request.method == "POST":
        ServiceRequest.objects.create(
            name=request.POST.get("name", ""),
            organization=request.POST.get("organization", ""),
            email=request.POST.get("email", ""),
            phone=request.POST.get("phone", ""),
            service=request.POST.get("service", ""),
            message=request.POST.get("message", ""),
        )
        messages.success(request, "Votre demande a bien été enregistrée.")
        return redirect("service_request")

    return render(request, "website/request.html", {"domains": DOMAINS})


def location(request):
    return render(request, "website/location.html")
