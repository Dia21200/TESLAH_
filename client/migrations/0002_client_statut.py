# Generated by Django 3.2.12 on 2022-05-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='statut',
            field=models.CharField(default='C', max_length=40),
        ),
    ]
