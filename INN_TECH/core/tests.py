from django.test import TestCase
from core.models.hospede import Hospede

class HospedeTestCase(TestCase):
    def test_criar_hospede(self):
        # Crie um novo hóspede
        novo_hospede = Hospede(
            nome="Vinicius Silva",
            cpf="123.456.789-00",
            dataNascimento="1998-05-25",
            telefone="123-456-7890"
        )
        novo_hospede.save()

        # Recupere o hóspede do banco de dados
        hospede_recuperado = Hospede.objects.get(pk=novo_hospede.pk)

        # Verifique se os campos foram salvos corretamente
        self.assertEqual(hospede_recuperado.nome, "Vinicius Silva")
        self.assertEqual(hospede_recuperado.cpf, "123.456.789-00")
        self.assertEqual(str(hospede_recuperado.dataNascimento), "1998-05-25")
        self.assertEqual(hospede_recuperado.telefone, "123-456-7890")

    def test_str(self):
        # Crie um hóspede
        hospede = Hospede(
            nome="Vinicius Silva",
            cpf="987.654.321-00",
            dataNascimento="1998-05-25",
            telefone="987-654-3210"
        )
        hospede.save()

        # Verifique o método __str__
        self.assertEqual(str(hospede), "Vinicius Silva")

        