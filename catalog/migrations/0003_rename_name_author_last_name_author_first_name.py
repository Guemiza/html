# Generated by Django 4.2.7 on 2023-11-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_bookinstance_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]