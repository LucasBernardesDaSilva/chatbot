# Generated by Django 2.2 on 2019-07-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190506_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertelegram',
            name='grr',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
