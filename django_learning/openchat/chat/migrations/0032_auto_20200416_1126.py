# Generated by Django 3.0.5 on 2020-04-16 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0031_auto_20200416_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Conversation', to_field='name'),
        ),
    ]
