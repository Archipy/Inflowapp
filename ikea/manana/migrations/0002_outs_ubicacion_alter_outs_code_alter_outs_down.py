# Generated by Django 4.1.2 on 2023-07-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manana', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outs',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Ubicacion'),
        ),
        migrations.AlterField(
            model_name='outs',
            name='code',
            field=models.CharField(blank=True, max_length=8, verbose_name='Referencia'),
        ),
        migrations.AlterField(
            model_name='outs',
            name='down',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Bajado'),
        ),
    ]
