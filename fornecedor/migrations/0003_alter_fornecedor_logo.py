# Generated by Django 3.2.4 on 2021-09-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0002_fornecedor_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='Logo',
            field=models.ImageField(blank=True, default='hortifruti-icon.png', upload_to='images/'),
        ),
    ]
