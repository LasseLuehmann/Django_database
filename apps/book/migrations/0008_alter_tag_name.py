# Generated by Django 5.0.6 on 2024-07-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]