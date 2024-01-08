# Generated by Django 4.2.6 on 2024-01-06 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_name', models.CharField(max_length=100)),
                ('web_subject', models.CharField(max_length=100)),
                ('web_data', models.CharField(max_length=100)),
                ('data_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.data')),
            ],
        ),
    ]