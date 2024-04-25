from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models


class Saida(models.Model):
    """
    Esta classe é responsável por todas as funcionalidades de saídas.
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

    motivo = models.TextField(
        verbose_name="Motivo",
        help_text="*Campo Obrigatório",
    )

    observacoes = models.TextField(
        verbose_name="Observações",
        null=True,
        blank=True,
    )

    usuario_criacao = models.ForeignKey(
        User,
        verbose_name="Usuário Criação",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user

        super(Saida, self).save(*args, **kwargs)

    def __str__(self):
        return f"Saida {self.id}"

    class Meta:
        app_label = "financeiro"
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"
