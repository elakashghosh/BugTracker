# Generated by Django 4.0.3 on 2022-05-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RelationApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='statusRightNow',
            field=models.CharField(default='assigned', max_length=10),
            preserve_default=False,
        ),
    ]
