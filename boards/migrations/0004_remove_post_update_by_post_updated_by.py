# Generated by Django 4.0.3 on 2022-04-18 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0003_post_update_by_post_updated_dt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='update_by',
        ),
        migrations.AddField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
