from django.contrib import admin
from ..models import Quarto

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
  list_display= [
    "id",
    "numero",
    "capacidade",
    "descricao",
    "ocupacao",
    "usuario_criacao",
  ]

  search_fields= [
    "id",
    "numero",
    "capacidade",
    "descricao",
    "ocupacao",
    "usuario_criacao__username",
  ]

  list_filter= [
    "ocupacao",
    "usuario_criacao",
  ]

  autocomplete_fields= [
    "usuario_criacao",
  ]

  fields = [
    "numero",
    "capacidade",
    "descricao",
    "ocupacao",
  ]

  def get_queryset(self, request):
    query = super().get_queryset(request)

    busca_por_autocomplete = request.path == "/admin/autocomplete/"
    if busca_por_autocomplete:
      return query.filter(ocupacao=False)
    else:
      return query
