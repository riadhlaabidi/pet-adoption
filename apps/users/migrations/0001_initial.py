# Generated by Django 4.1.6 on 2023-02-14 22:47

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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('avatar', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('is_organization', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
