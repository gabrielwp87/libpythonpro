import pytest

from libpythonpro.tests.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['gabrielpiazenski@gmail.com','renzo@python.pro.br']
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
