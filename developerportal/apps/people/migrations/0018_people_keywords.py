# Generated by Django 2.2.3 on 2019-07-23 16:59

from django.db import migrations
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('people', '0017_auto_20190718_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='keywords',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='people.PeopleTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
