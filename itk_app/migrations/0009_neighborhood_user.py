# Generated by Django 2.2.7 on 2019-12-02 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itk_app', '0008_healthcenter_police'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
