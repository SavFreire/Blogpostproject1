# Generated by Django 4.0.2 on 2022-02-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subtitle',
            field=models.CharField(default='subtitle', max_length=20),
            preserve_default=False,
        ),
    ]
