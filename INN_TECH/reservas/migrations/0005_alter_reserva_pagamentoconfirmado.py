# Generated by Django 4.0.5 on 2022-07-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='pagamentoConfirmado',
            field=models.BooleanField(default=False, verbose_name='Pagamento Confirmado'),
        ),
    ]
