# Generated by Django 3.2.4 on 2021-09-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='Logo',
            field=models.ImageField(default='hortifruti-icon.png', upload_to='images/'),
        ),
    ]
