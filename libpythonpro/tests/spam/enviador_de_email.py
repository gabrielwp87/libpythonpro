class Enviador:
    def __init__(self):
        self.quantidade_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email do rementente inválido: {remetente}')
        self.quantidade_email_enviados += 1
        return remetente


class EmailInvalido(Exception):
    pass
