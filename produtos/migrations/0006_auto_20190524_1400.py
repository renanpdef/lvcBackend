# Generated by Django 2.2.1 on 2019-05-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_produto_quantidadeinicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidadeInicial',
            field=models.IntegerField(editable=False, verbose_name='Quantidade Inicial'),
        ),
    ]
