# Generated by Django 5.1.3 on 2024-11-30 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libApp', '0003_book_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('regNo', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('dateJoined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
