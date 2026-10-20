from django.contrib import admin
from .models import ContactMessage,ServiceRequest
@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin): list_display=("name","email","subject","created_at"); search_fields=("name","email","subject")
@admin.register(ServiceRequest)
class RequestAdmin(admin.ModelAdmin): list_display=("name","organization","service","email","created_at"); search_fields=("name","organization","service","email")
