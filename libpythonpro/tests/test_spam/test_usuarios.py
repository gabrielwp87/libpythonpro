import pytest

from libpythonpro.tests.spam.db import Conexao
from libpythonpro.tests.spam.modelos import Usuario

#Existe 3 escopos da fixture, por função, por módulo e por sessão (será executado apenas uma vez na sessão de teste)
@pytest.fixture(scope='module')
def conexao():
    #Setup
    conexao_obj = Conexao()
    yield conexao_obj
    #Tear down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()

def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Gabriel')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Gabriel'), Usuario(nome='Renzo')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()