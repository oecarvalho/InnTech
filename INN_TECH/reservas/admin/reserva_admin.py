from django.contrib import admin
from ..models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
  list_display= [
    "id",
    "dataChegada",
    "dataSaida",
    "valorReserva",
    "pagamentoConfirmado",
    "observacoes",
    "quarto",
    "hospede",
  ]

  search_fields= [
    "id",
    "dataChegada",
    "dataSaida",
    "valorReserva",
    "pagamentoConfirmado",
    "observacoes",
    "quarto__numero",
    "hospede__nome",
  ]

  list_filter= [
    "dataChegada",
    "dataSaida",
    "pagamentoConfirmado",
    "hospede",
  ]

  autocomplete_fields= [
    "quarto",
    "hospede",
  ]

  def get_readonly_fields(self, request, obj=None):
    if not obj:
      return ["dataSaida"]

    pagamento_nao_confirmado = not obj.pagamentoConfirmado
    if pagamento_nao_confirmado:
      return ["dataSaida"]

    return []
