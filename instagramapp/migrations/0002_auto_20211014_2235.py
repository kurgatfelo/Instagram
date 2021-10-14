# Generated by Django 3.2.8 on 2021-10-14 19:35

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagramapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, default='Bio', max_length=300),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(blank=True, max_length=80)),
                ('caption', models.CharField(max_length=500)),
                ('comments', models.CharField(blank=True, max_length=100)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagramapp.profile')),
            ],
        ),
    ]