# Generated by Django 3.1.7 on 2021-03-29 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0033_agentcustomfield_multiple_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentcustomfield',
            name='checkbox_value',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]