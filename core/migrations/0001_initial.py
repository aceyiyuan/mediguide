# Generated by Django 4.2.3 on 2023-07-04 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('active_ingredient', models.CharField(max_length=255)),
                ('purpose', models.TextField()),
                ('cns_medication', models.BooleanField()),
                ('more_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicationStrength',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('strength', models.CharField(max_length=20)),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medicationinfo')),
            ],
        ),
        migrations.CreateModel(
            name='MedicationImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('front_image', models.ImageField(upload_to='images/')),
                ('back_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('package_image', models.ImageField(upload_to='images/')),
                ('medication_strength', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medicationstrength')),
            ],
        ),
        migrations.CreateModel(
            name='AlternativeMedications',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('medication_name', models.CharField(max_length=255)),
                ('medication_link', models.URLField()),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medicationinfo')),
            ],
        ),
    ]