# Generated by Django 3.2.5 on 2021-07-26 08:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproblem',
            name='code_to_debug',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
