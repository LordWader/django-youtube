# Generated by Django 2.2.3 on 2019-07-13 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0007_auto_20190714_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyworddata',
            name='videos',
        ),
    ]
