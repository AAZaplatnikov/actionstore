# Generated by Django 4.2.5 on 2023-10-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionSt_dt', models.DateTimeField(auto_now=True)),
                ('action_zone', models.CharField(max_length=100)),
                ('Action_tipe', models.CharField(max_length=100)),
                ('numbers_clips', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
            ],
        ),
    ]
