# Generated by Django 2.1 on 2018-09-14 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180914_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiel',
            name='Date_entree',
            field=models.DateTimeField(),
        ),
    ]
