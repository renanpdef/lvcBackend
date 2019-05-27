# Generated by Django 2.2.1 on 2019-05-24 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0009_auto_20190524_0200'),
        ('usuarios', '__latest__'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='usuarios.Cliente'),
        ),
    ]