# Generated by Django 5.1.1 on 2024-09-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_company_comp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='comp_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
