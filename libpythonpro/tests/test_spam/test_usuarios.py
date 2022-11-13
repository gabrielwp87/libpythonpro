from libpythonpro.tests.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Gabriel', email='gabrielpiazenski@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Gabriel', email='gabrielpiazenski@gmail.com'),
        Usuario(nome='Renzo', email='rezon@python.pro.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
