from django.contrib import admin
from ..models import Saida

@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
  list_display= [
    "id",
    "valor",
    "dataCriacao",
    "motivo",
    "observacoes",
    "usuario_criacao",
  ]

  search_fields= [
    "id",
    "valor",
    "dataCriacao",
    "motivo",
    "observacoes",
    "usuario_criacao__username",
  ]

  list_filter= [
   "dataCriacao",
   "usuario_criacao", 
  ]

  autocomplete_fields= [
    "usuario_criacao",
  ]

  fields= [
    "valor",
    "motivo",
    "observacoes",
  ]