# Generated by Django 2.2.4 on 2019-12-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191210_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='taginfo',
            name='img_url',
            field=models.CharField(default='/static/images/html.jpg', max_length=20),
        ),
    ]