import pytest

from libpythonpro.tests.spam.enviador_de_email import Enviador
from libpythonpro.tests.spam.main import Enviador_de_spam
from libpythonpro.tests.spam.modelos import Usuario


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
    enviador = Enviador()
    enviador_de_spam = Enviador_de_spam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gabrielpiazenski@gmail.com',
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )
    assert len(usuarios) == enviador.quantidade_email_enviados
