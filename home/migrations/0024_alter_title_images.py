# Generated by Django 4.2.9 on 2024-09-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_menu_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='images',
            field=models.ImageField(upload_to=''),
        ),
    ]
