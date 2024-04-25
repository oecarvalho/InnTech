from django.test import TestCase
from django.contrib.auth.models import User
from reservas.models import Quarto
from crum import set_current_user

class QuartoTestCase(TestCase):
    def setUp(self):
        # Crie um usuário de teste
        self.usuario_teste = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

    def test_usuario_criacao(self):
        # Defina o usuário atual como o usuário de teste
        set_current_user(self.usuario_teste)

        # Crie uma instância de Quarto
        quarto = Quarto(
            numero=101,
            capacidade=2
        )
        quarto.save()

        # Recupere o quarto do banco de dados
        quarto_recuperado = Quarto.objects.get(pk=quarto.pk)

        # Verifique se o usuário de criação é o usuário de teste
        self.assertEqual(quarto_recuperado.usuario_criacao, self.usuario_teste)

