# Generated by Django 2.1.7 on 2021-06-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.CharField(default='', max_length=300),
        ),
    ]
