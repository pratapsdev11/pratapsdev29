# Generated by Django 3.2.4 on 2023-12-19 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Divya', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_blog',
            name='blog_medium_link',
        ),
        migrations.RemoveField(
            model_name='my_portfolio',
            name='portfolio_live_link',
        ),
        migrations.RemoveField(
            model_name='my_portfolio',
            name='portfolio_medium_link',
        ),
    ]
