# Generated by Django 2.2 on 2019-04-02 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTelegram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('chat_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_telegram',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_dt', models.DateTimeField(auto_now=True, null=True)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserTelegram')),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='MensagemNaoRespondida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now=True, null=True)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserTelegram')),
            ],
            options={
                'db_table': 'mensagem_nao_respondida',
            },
        ),
        migrations.CreateModel(
            name='LastUserContext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('context', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.UserTelegram')),
            ],
            options={
                'db_table': 'last_user_context',
            },
        ),
    ]