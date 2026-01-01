# Migration to add database indexes for performance optimization

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_platform'),
    ]

    operations = [
        # Add index to Course.is_active field
        migrations.AlterField(
            model_name='course',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),
        # Add composite indexes to Course model
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['is_active', 'platform'], name='course_active_platform_idx'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['platform', 'order'], name='course_platform_order_idx'),
        ),
        # Add indexes to UserProgress model
        migrations.AlterField(
            model_name='userprogress',
            name='completed',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='userprogress',
            name='last_accessed',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        # Add composite indexes to UserProgress model
        migrations.AddIndex(
            model_name='userprogress',
            index=models.Index(fields=['user', 'completed'], name='user_progress_user_completed_idx'),
        ),
        migrations.AddIndex(
            model_name='userprogress',
            index=models.Index(fields=['last_accessed'], name='user_progress_accessed_idx'),
        ),
    ]
