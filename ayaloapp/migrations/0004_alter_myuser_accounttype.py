# Generated by Django 3.2.4 on 2021-06-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayaloapp', '0003_auto_20210626_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='AccountType',
            field=models.CharField(choices=[('Leesee', 'Leeser'), ('Leesee', 'Leesser')], max_length=256),
        ),
    ]