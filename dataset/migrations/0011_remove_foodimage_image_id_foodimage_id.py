# Generated by Django 5.0.6 on 2024-06-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0010_remove_foodimage_id_foodimage_image_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodimage',
            name='image_id',
        ),
        migrations.AddField(
            model_name='foodimage',
            name='id',
            field=models.BigAutoField(auto_created=True, default=63, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
