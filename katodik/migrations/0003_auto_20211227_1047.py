# Generated by Django 3.2.9 on 2021-12-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katodik', '0002_panolar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hatlar',
            name='CAP',
            field=models.IntegerField(blank=True, null=True, verbose_name='Çapı '),
        ),
        migrations.AlterField(
            model_name='hatlar',
            name='KAPLAMA',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Kaplaması  '),
        ),
        migrations.AlterField(
            model_name='hatlar',
            name='UZUNLUK',
            field=models.IntegerField(blank=True, null=True, verbose_name='Uzunluğu '),
        ),
    ]
