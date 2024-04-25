from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from ..models import Reserva


@receiver(post_save, sender=Reserva)
def reserva_post_save(sender, instance, created, **kwargs):
    if created:
        instance.gerar_pagamento_se_confirmado()
        instance.ocupar_quarto()
    elif kwargs["update_fields"]:
        mudou_pagamento_confirmado = (
            "pagamentoConfirmado" in kwargs["update_fields"]
        )
        mudou_valor_reserva = "valorReserva" in kwargs["update_fields"]
        mudou_data_saida = "dataSaida" in kwargs["update_fields"]

        if mudou_pagamento_confirmado:
            instance.gerar_pagamento_se_confirmado()

        if mudou_valor_reserva:
            instance.atualizar_valor_pagamento()

        if mudou_data_saida:
            instance.desocupar_quarto()


@receiver(pre_save, sender=Reserva)
def reserva_pre_save(sender, instance, **kwargs):
    try:
        old_object = Reserva.objects.filter(id=instance.id).first()
    except TypeError:
        old_object = None

    if old_object and (old_object.quarto != instance.quarto):
        old_object.desocupar_quarto()
        instance.ocupar_quarto()
