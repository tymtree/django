# Generated by Django 2.1.7 on 2019-02-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac1', '0003_auto_20190225_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plant_image',
            field=models.ImageField(null=True, upload_to='plant_pics', verbose_name='img'),
        ),
    ]
