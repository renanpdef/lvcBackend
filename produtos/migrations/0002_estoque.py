# Generated by Django 2.2.1 on 2019-05-03 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto')),
            ],
        ),
    ]
