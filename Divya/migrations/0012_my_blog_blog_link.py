# Generated by Django 3.2.4 on 2024-01-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Divya', '0011_my_profile_nav_my_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_blog',
            name='blog_link',
            field=models.URLField(blank=True, db_index=True, max_length=128, verbose_name='blog_link'),
        ),
    ]
