# Generated by Django 3.2.5 on 2021-12-24 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OLUSTURMA_TARIHI', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('HAT_ADI', models.CharField(max_length=50, verbose_name='Hat Adı: ')),
                ('HAT_TIPI', models.CharField(choices=[('İÇMESUYU', 'İÇMESUYU'), ('ATIKSU', 'ATIKSU'), ('YAĞMURSUYU', 'YAĞMURSUYU')], max_length=50, verbose_name='Hat Tipi  ')),
                ('CAP', models.IntegerField(blank=True, verbose_name='Çapı ')),
                ('UZUNLUK', models.IntegerField(blank=True, verbose_name='Uzunluğu ')),
                ('KAPLAMA', models.CharField(blank=True, max_length=50, verbose_name='Kaplaması  ')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Oluşturan ')),
            ],
            options={
                'verbose_name': 'Hat',
                'verbose_name_plural': 'Hatlar',
            },
        ),
    ]
