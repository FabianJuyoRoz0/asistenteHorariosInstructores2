# Generated by Django 4.1 on 2022-09-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_instructores_cantidadhorasformacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratacion',
            name='supervisora',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
