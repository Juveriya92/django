# Generated by Django 4.1.4 on 2023-03-23 10:40

from django.db import migrations, models
import django_matplotlib.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plotting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('figure', django_matplotlib.fields.MatplotlibFigureField()),
            ],
        ),
    ]
