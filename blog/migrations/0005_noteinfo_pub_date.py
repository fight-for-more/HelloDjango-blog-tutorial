# Generated by Django 2.2.4 on 2019-12-15 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191215_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteinfo',
            name='pub_date',
            field=models.DateField(default='2019-12-11'),
        ),
    ]