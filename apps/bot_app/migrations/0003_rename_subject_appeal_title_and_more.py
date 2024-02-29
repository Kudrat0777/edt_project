# Generated by Django 4.2.10 on 2024-02-28 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bot_app', '0002_appeal_citizen_response_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appeal',
            old_name='subject',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='citizen',
            old_name='full_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='appeal',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='appeal',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='email',
        ),
        migrations.RemoveField(
            model_name='citizen',
            name='phone',
        ),
        migrations.AddField(
            model_name='appeal',
            name='submission_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='citizen',
            name='contact_info',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appeal',
            name='status',
            field=models.CharField(choices=[('new', 'Новое'), ('in_progress', 'В обработке'), ('resolved', 'Решено'), ('rejected', 'Отклонено')], default='new', max_length=20),
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
