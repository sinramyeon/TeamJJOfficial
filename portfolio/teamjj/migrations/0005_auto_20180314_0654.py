# Generated by Django 2.0.3 on 2018-03-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamjj', '0004_auto_20180314_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_id',
        ),
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]