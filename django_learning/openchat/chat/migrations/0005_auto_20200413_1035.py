# Generated by Django 3.0.5 on 2020-04-13 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20200413_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Conversation', to_field='name'),
        ),
    ]