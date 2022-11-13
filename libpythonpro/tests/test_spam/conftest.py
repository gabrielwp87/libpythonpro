import pytest

from libpythonpro.tests.spam.db import Conexao


# Existe 3 escopos da fixture, por função, por módulo e por sessão (de teste)
@pytest.fixture(scope='module')
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
