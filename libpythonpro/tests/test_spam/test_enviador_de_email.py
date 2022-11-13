from libpythonpro.tests.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetent():
    enviador = Enviador()
    resultado = enviador.enviar(
        'gabrielpiazenski@gmail.com',
        'GABRIEL.PIAZENSKI@edu.pucrs.br',
        'Estudo de TDD',
        'Primeiros passos.'
    )
    assert 'gabrielpiazenski@gmail.com' in resultado
    