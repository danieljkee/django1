# Generated by Django 4.1.4 on 2022-12-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=35)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
    ]
