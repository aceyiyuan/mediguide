# Generated by Django 4.2.3 on 2023-07-04 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_alternativemedications_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicationimages',
            name='medication_strength',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medicationstrength'),
        ),
    ]
