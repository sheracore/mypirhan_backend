# Generated by Django 3.1.4 on 2021-08-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210829_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='phone',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]