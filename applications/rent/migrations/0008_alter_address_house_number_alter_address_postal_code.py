# Generated by Django 5.2.1 on 2025-05-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_alter_rent_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='house_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
