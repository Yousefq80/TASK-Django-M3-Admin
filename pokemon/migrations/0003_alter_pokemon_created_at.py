# Generated by Django 4.0.4 on 2022-10-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_alter_pokemon_name_ar_alter_pokemon_name_fr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
