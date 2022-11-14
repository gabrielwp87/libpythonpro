from unittest.mock import Mock

import pytest

from libpythonpro.tests.spam.main import EnviadorDeSpam
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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gabrielpiazenski@gmail.com',
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gabriel', email='gabrielpiazenski@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br',
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )
    enviador.enviar.assert_called_once_with(
        'renzo@python.pro.br',
        'gabrielpiazenski@gmail.com',
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )
