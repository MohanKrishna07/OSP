# Generated by Django 2.2.5 on 2022-03-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20220329_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=200, null=True),
        ),
    ]
