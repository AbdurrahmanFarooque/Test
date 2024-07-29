# Generated by Django 4.2.14 on 2024-07-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
    ]