# Generated by Django 3.2.4 on 2021-06-25 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_agregue_relate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesamodel',
            name='updateAt',
            field=models.DateTimeField(auto_now=True, db_column='updated_at'),
        ),
        migrations.AddField(
            model_name='usuariomodel',
            name='updateAt',
            field=models.DateTimeField(auto_now=True, db_column='updated_at'),
        ),
    ]
