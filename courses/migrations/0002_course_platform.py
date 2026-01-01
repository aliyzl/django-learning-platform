# Generated migration for adding platform field to Course model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='platform',
            field=models.CharField(
                choices=[('all', 'All Platforms'), ('mac', 'Mac'), ('windows', 'Windows')],
                default='all',
                max_length=20,
                verbose_name='Platform'
            ),
        ),
    ]




