# Generated by Django 2.0.7 on 2019-09-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ChatLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_id', models.CharField(blank=True, max_length=15)),
                ('order_id', models.CharField(max_length=15)),
                ('line_text', models.TextField()),
                ('writer_id', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='medicine',
            name='med_id',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
