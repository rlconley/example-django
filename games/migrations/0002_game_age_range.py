# Generated by Django 4.2.1 on 2023-05-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='age_range',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]