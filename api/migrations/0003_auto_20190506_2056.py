# Generated by Django 2.2 on 2019-05-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190506_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lastusercontext',
            name='respondida',
        ),
        migrations.AddField(
            model_name='message',
            name='respondida',
            field=models.BooleanField(default=False),
        ),
    ]
