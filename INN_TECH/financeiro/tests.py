from decimal import Decimal
from django.test import TestCase
from django.utils import timezone
from financeiro.models.pagamento import Pagamento
from financeiro.models.saida import Saida

class PagamentoTestCase(TestCase):
    def test_atualizar_valor(self):
        # Crie um pagamento
        pagamento = Pagamento.objects.create(
            valor=Decimal('100.00'),
            dataCriacao=timezone.now()
        )

        # Atualize o valor
        novo_valor = Decimal('150.00')
        pagamento.atualizar_valor(novo_valor)

        # Recupere o pagamento do banco de dados
        pagamento_recuperado = Pagamento.objects.get(pk=pagamento.pk)

        # Verifique se o valor foi atualizado corretamente
        self.assertEqual(pagamento_recuperado.valor, novo_valor)

class SaidaTestCase(TestCase):
    def test_usuario_criacao(self):
        # Crie um usuário de teste
        usuario_teste = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Defina o usuário atual como o usuário de teste
        set_current_user(usuario_teste)

        # Crie uma instância de Saida
        saida = Saida(
            valor=100.00,
            motivo="Motivo de teste"
        )
        saida.save()

        # Recupere a saída do banco de dados
        saida_recuperada = Saida.objects.get(pk=saida.pk)

        # Verifique se o usuário de criação é o usuário de teste
        self.assertEqual(saida_recuperada.usuario_criacao, usuario_teste)
