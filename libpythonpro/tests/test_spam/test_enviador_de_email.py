import pytest

from libpythonpro.tests.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['gabrielpiazenski@gmail.com', 'renzo@python.pro.br']
    )
def test_remetent(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'GABRIEL.PIAZENSKI@edu.pucrs.br',
        'Estudo de TDD',
        'Primeiros passos.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'gabriel']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'GABRIEL.PIAZENSKI@edu.pucrs.br',
            'Estudo de TDD',
            'Primeiros passos.'
        )
