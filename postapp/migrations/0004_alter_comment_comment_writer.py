# Generated by Django 4.0.5 on 2023-02-19 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('postapp', '0003_comment_comment_writer_alter_comment_anonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]