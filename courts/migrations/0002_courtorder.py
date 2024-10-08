# Generated by Django 5.1.1 on 2024-09-16 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
        ('members', '0004_delete_court'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourtOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.court')),
                ('member1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member1', to='members.member')),
                ('member2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member2', to='members.member')),
            ],
        ),
    ]
