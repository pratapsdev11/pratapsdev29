# Generated by Django 3.2.4 on 2023-12-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Divya', '0008_auto_20231223_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(upload_to='videos/')),
            ],
        ),
    ]
