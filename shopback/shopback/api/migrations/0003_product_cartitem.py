# Generated by Django 3.0.4 on 2020-04-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cart_feedback_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cartitem',
            field=models.IntegerField(default=1),
        ),
    ]
