# Generated by Django 2.2.3 on 2019-07-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0008_remove_keyworddata_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyworddata',
            name='videos',
            field=models.ManyToManyField(to='testapi.YouTubeVideo'),
        ),
    ]