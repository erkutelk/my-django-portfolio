# Generated by Django 5.1.6 on 2025-03-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_alter_about_about_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_description',
            field=models.TextField(max_length=250),
        ),
    ]
