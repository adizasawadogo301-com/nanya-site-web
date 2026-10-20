from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("a-propos/", views.about, name="about"),
    path("domaines/", views.domains, name="domains"),
    path("domaines/<slug:slug>/", views.domain_detail, name="domain_detail"),
    path("services/", views.services, name="services"),
    path("partenaires/", views.partners, name="partners"),
    path("realisations/", views.realizations, name="realizations"),
    path("contact/", views.contact, name="contact"),
    path("demande-de-service/", views.service_request, name="service_request"),
    path("coordonnees/", views.location, name="location"),
]
