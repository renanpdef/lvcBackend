# Generated by Django 2.2.1 on 2019-05-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_remove_produto_quantidadeinicial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidadeInicial',
            field=models.IntegerField(default=0, verbose_name='Quantidade Inicial'),
            preserve_default=False,
        ),
    ]
