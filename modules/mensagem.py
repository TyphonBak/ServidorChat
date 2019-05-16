class Mensagem:
    def __init__(self, id_remetente, id_destinatario, datahora, texto, id=0):
        self.id = id
        self.id_remetente = id_remetente
        self.id_destinatario = id_destinatario
        self.datahora = datahora
        self.texto = texto

    def __dict__(self):
        return {
            'de': self.id_remetente,
            'para': self.id_destinatario,
            'datahora': self.datahora,
            'texto': self.texto
        }

    @staticmethod
    def cria(dados):
        try:
            id_remetente = dados['id_remetente']
            id_destinatario = dados['id_destinatario']
            datahora = dados['datahora']
            texto = dados['texto']
            return Mensagem(id_remetente, id_destinatario, datahora, texto)
        except Exception as e:
            print(e)

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            id_remetente = dados[1]
            id_destinatario = dados[2]
            datahora = dados[3]
            texto = dados[4]
            return Mensagem(id_remetente, id_destinatario, datahora, texto, id=id)
        except Exception as e:
            print(e)
