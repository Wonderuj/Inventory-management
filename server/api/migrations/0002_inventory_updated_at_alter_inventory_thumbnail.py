# Generated by Django 5.0.3 on 2024-03-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail/images'),
        ),
    ]
