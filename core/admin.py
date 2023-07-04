from django.contrib import admin
from .models import MedicationInfo, MedicationStrength, MedicationImages, AlternativeMedications

admin.site.register(MedicationInfo)
admin.site.register(MedicationStrength)
admin.site.register(MedicationImages)
admin.site.register(AlternativeMedications)
