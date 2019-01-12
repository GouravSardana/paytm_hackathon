from django.contrib import admin

from home.models import Doctor_Detail, Patient_Detail

admin.site.register(Patient_Detail)
admin.site.register(Doctor_Detail)