import pytest

from libpythonpro.tests.spam.enviador_de_email import Enviador
from libpythonpro.tests.spam.main import EnviadorDeSpam
from libpythonpro.tests.spam.modelos import Usuario


class EnviadorMock:
    def __init__(self):
        super().__init__()
        self.quantidade_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.quantidade_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Gabriel', email='gabrielpiazenski@gmail.com'),
            Usuario(nome='Renzo', email='rezon@python.pro.br')
        ],
        [
            Usuario(nome='Gabriel', email='gabrielpiazenski@gmail.com'),
        ]
    ]
)
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gabrielpiazenski@gmail.com',
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )
    assert len(usuarios) == enviador.quantidade_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gabriel', email='gabrielpiazenski@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )
    assert enviador.parametros_de_envio == (
        'renzo@python.pro.br',
        'gabrielpiazenski@gmail.com',
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )
