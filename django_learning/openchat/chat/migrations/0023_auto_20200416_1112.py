# Generated by Django 3.0.5 on 2020-04-16 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0022_auto_20200416_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='author',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Conversation', to_field='name'),
        ),
    ]
