# Generated by Django 5.0.4 on 2024-04-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=10, unique=True)),
                ('is_occupied', models.BooleanField(default=False)),
            ],
        ),
    ]
