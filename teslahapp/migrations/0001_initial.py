# Generated by Django 3.2.12 on 2022-05-06 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
        ('prestataire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricite', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialite', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
                ('photos', models.ImageField(null=True, upload_to='image/')),
                ('Date_pub', models.DateTimeField(auto_now_add=True)),
                ('Lieu', models.CharField(max_length=200)),
                ('prestataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='prestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_telephone', models.IntegerField(unique=True)),
                ('Adress', models.CharField(max_length=255)),
                ('Service', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='consulter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prestataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestataire.prestataire')),
            ],
        ),
        migrations.CreateModel(
            name='commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
                ('date_comments', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
                ('publi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teslahapp.publication')),
            ],
        ),
    ]
