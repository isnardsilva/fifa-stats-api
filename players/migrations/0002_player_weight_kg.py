# Generated by Django 3.0.8 on 2020-07-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='weight_kg',
            field=models.IntegerField(default=70),
            preserve_default=False,
        ),
    ]