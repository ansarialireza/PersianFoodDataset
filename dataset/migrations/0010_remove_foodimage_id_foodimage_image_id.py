# Generated by Django 5.0.6 on 2024-06-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0009_remove_foodimage_unique_id_foodimage_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodimage',
            name='id',
        ),
        migrations.AddField(
            model_name='foodimage',
            name='image_id',
            field=models.AutoField(default=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
