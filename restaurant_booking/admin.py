from django.contrib import admin
# Import Booking model from models.py
from .models import Booking

# Register your models here.
admin.site.register(Booking)