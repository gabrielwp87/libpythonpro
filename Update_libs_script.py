"""
Esse scritp serve para verificar quais as libs que estão desatualizadas e se quer atualizá-las.
A lib 'lib-upgrade' foi adicionada a requirements-dev.txt.
Essa lib também pode ser acionada pelo terminal, é só entrar no python e digitar o que está nesse scritp.
"""

from lib_upgrade.lib_upgrade import upgrade_lib
upgrade_lib()