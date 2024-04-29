# Generated by Django 5.0.4 on 2024-04-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='status',
            field=models.CharField(choices=[('R', 'Reviewed'), ('N', 'Not Reviewed'), ('E', 'Error'), ('A', 'Accepted')], default='R', max_length=1),
            preserve_default=False,
        ),
    ]
