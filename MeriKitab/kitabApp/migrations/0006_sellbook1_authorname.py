# Generated by Django 4.0 on 2023-12-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitabApp', '0005_alter_sellbook1_setprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellbook1',
            name='authorName',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
