# Generated by Django 2.1.7 on 2021-06-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190326_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='resume',
            field=models.CharField(max_length=300, null=True),
        ),
    ]