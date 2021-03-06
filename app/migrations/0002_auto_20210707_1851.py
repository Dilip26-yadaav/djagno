# Generated by Django 3.2.4 on 2021-07-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='status',
            field=models.CharField(choices=[('C', 'Complete'), ('P', 'Pending')], max_length=2),
        ),
    ]
