# Generated by Django 4.2.2 on 2023-11-16 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0015_rename_district_branch_district_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='person',
        ),
    ]