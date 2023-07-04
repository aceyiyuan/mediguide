from django.db import models


class MedicationInfo(models.Model):
    name = models.CharField(max_length=255)
    active_ingredient = models.CharField(max_length=255)
    purpose = models.TextField()
    cns_medication = models.BooleanField()
    more_details = models.TextField()

    def __str__(self):
        return self.name


class MedicationStrength(models.Model):
    medication = models.ForeignKey(MedicationInfo, on_delete=models.CASCADE)
    strength = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.medication.name} - {self.strength}"


class MedicationImages(models.Model):
    medication_strength = models.ForeignKey(MedicationStrength, on_delete=models.CASCADE)
    front_image = models.ImageField(upload_to='images/')
    back_image = models.ImageField(upload_to='images/', blank=True, null=True)
    package_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.medication_strength.medication.name} - {self.medication_strength.strength}"


class AlternativeMedications(models.Model):
    medication = models.ForeignKey(MedicationInfo, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=255)
    medication_link = models.URLField()

    def __str__(self):
        return f"{self.medication.name} - Alternative: {self.medication_name}"

