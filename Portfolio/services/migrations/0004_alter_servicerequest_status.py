# Generated by Django 4.2.4 on 2023-09-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_servicerequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('in_progress', 'in_progress'), ('done', 'done'), ('canceled', 'canceled')], default='Pending', max_length=300),
        ),
    ]