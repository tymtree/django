# Generated by Django 2.1.7 on 2019-02-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='plant_image',
            field=models.ImageField(null=True, upload_to='plant_pics', verbose_name='img'),
        ),
    ]
