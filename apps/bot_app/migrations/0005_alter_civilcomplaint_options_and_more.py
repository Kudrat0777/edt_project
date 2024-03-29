# Generated by Django 4.2.10 on 2024-02-29 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bot_app', '0004_civilcomplaint_employeeresponse_delete_appeal_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='civilcomplaint',
            options={'ordering': ['-timestamp'], 'verbose_name': 'гражданское обращение', 'verbose_name_plural': 'гражданские обращения'},
        ),
        migrations.AlterModelOptions(
            name='employeeresponse',
            options={'ordering': ['-timestamp'], 'verbose_name': 'ответ сотрудника', 'verbose_name_plural': 'ответы сотрудников'},
        ),
        migrations.AlterField(
            model_name='civilcomplaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
