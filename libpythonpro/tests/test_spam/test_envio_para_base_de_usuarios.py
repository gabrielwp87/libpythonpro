from libpythonpro.tests.spam.enviador_de_email import Enviador
from libpythonpro.tests.spam.main import Enviador_de_spam


def test_envio_de_spam(sessao):
    enviador_de_spam = Enviador_de_spam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'gabrielpiazenski@gmail.com',
        'Curso Python Pro',
        'Confira que estudo fantástico'
    )
