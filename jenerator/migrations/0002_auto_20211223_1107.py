# Generated by Django 3.2.5 on 2021-12-23 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jenerator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arizalar',
            name='PERSONEL',
            field=models.CharField(blank=True, max_length=50, verbose_name='Personel'),
        ),
        migrations.AlterField(
            model_name='arizalar',
            name='JENERATOR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jenerator.jeneratorler', verbose_name='Jenerator '),
        ),
        migrations.AlterField(
            model_name='jeneratorler',
            name='GUC',
            field=models.IntegerField(verbose_name='Gücü '),
        ),
        migrations.AlterField(
            model_name='jeneratorler',
            name='TESIS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jenerator.tesisler', verbose_name='Tesis '),
        ),
        migrations.AlterField(
            model_name='tesisler',
            name='SCADA_KODU',
            field=models.CharField(blank=True, max_length=50, verbose_name='Scada Kodu '),
        ),
    ]
