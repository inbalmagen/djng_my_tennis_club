# Generated by Django 5.1.1 on 2024-09-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=5)),
                ('Is_occupied', models.BooleanField(null=True)),
                ('date_time_occupation', models.DateTimeField(null=True)),
            ],
        ),
    ]
