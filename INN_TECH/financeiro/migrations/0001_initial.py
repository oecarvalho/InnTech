# Generated by Django 4.0.5 on 2022-07-09 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservas', '0006_reserva_quarto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('dataCriacao', models.DateTimeField(verbose_name='Data Criação')),
                ('motivo', models.TextField(verbose_name='Motivo')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('usuario_criacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário Criação')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('dataCriacao', models.DateTimeField(verbose_name='Data Criação')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('reserva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservas.reserva', verbose_name='Reserva')),
            ],
        ),
    ]
