# Generated by Django 2.1 on 2019-09-28 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('zf_plugins', '0004_quoteheroconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='zf_plugins_articleconfig', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=100)),
                ('kicker', models.TextField(max_length=400)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]