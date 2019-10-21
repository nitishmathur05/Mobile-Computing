# Generated by Django 2.2.1 on 2019-09-18 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('predict_inceptionV3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images_recieved/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]