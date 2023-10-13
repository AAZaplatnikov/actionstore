# Generated by Django 4.2.5 on 2023-10-12 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='actionstore',
            name='datestore',
            field=models.DateTimeField(default='default_value'),
        ),
        migrations.AddField(
            model_name='actionstore',
            name='storenumber',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='actionstore',
            name='timestore',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AddField(
            model_name='actionstore',
            name='floor',
            field=models.ForeignKey(default='default_value', on_delete=django.db.models.deletion.CASCADE, to='storeactions.floor'),
        ),
    ]