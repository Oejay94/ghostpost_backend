# Generated by Django 3.0.4 on 2020-03-25 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_backend', '0003_auto_20200324_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boastroast',
            name='title',
        ),
    ]
