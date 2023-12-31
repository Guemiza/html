# Generated by Django 4.2.6 on 2023-10-28 10:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='write a title', max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('imprint', models.CharField(max_length=200)),
                ('ISBN', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('uniqueId', models.UUIDField(default=uuid.uuid4, help_text='Id Unique', primary_key=True, serialize=False)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.language'),
        ),
    ]
