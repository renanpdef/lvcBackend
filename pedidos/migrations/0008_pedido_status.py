# Generated by Django 2.2.1 on 2019-05-22 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_remove_pedido_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('PR', 'Pedido Realizado'), ('SE', 'Separacao em Estoque'), ('EM', 'Em Montagem'), ('RT', 'Realizacao de Testes'), ('CO', 'Concluido')], default='PR', editable=False, max_length=2, verbose_name='Status'),
        ),
    ]
