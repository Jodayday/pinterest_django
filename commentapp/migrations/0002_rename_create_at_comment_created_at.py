# Generated by Django 4.0.5 on 2022-07-04 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
