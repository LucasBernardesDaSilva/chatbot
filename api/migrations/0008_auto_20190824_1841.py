# Generated by Django 2.2.4 on 2019-08-24 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190824_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permissoes',
            old_name='fundamentos',
            new_name='algoritimos',
        ),
    ]
