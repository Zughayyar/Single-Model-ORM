# Generated by Django 5.1.2 on 2024-11-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]