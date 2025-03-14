# Generated by Django 4.2.20 on 2025-03-12 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=2048)),
                ('short_url', models.CharField(blank=True, max_length=10, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
            ],
        ),
    ]
