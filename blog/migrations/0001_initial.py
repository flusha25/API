# Generated by Django 5.0.1 on 2024-01-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('publish_date', models.DateField()),
                ('description', models.TextField(default='')),
                ('mail', models.EmailField(max_length=254)),
                ('image', models.URLField()),
                ('categories', models.ManyToManyField(to='blog.category')),
            ],
        ),
    ]
