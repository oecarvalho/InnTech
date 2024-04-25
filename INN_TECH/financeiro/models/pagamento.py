from decimal import Decimal

from django.db import models


class Pagamento(models.Model):
    """
    Esta classe é responsável para armazenar/gerênciar todos os Pagamentos.
    """

    valor = models.DecimalField(
        verbose_name="Valor",
        help_text="*Campo Obrigatório",
        max_digits=7,
        decimal_places=2,
    )

    dataCriacao = models.DateTimeField(
        verbose_name="Data Criação",
        auto_now_add=True,
    )

    reserva = models.OneToOneField(
        "reservas.Reserva",
        verbose_name="Reserva",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def atualizar_valor(self, valor: Decimal) -> None:
        """
        Atualiza o valor do pagamento.
        """

        self.valor = valor
        self.save()

    def __str__(self):
        return f"Pagamento {self.id}"

    class Meta:
        app_label = "financeiro"
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"
