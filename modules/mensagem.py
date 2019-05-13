class Mensagem:
    def __init__(self, id_remetente, id_destinatario, datahora, texto, id=0):
        self.id = id
        self.id_remetente = id_remetente
        self.id_destinatario = id_destinatario
        self.datahora = datahora
        self.texto = texto

    @staticmethod
    def cria(self, dados):
        try:
            id_remetente = dados['id_remetente']
            id_destinatario = dados['id_destinatario']
            datahora = dados['datahora']
            texto = dados['texto']
            return Mensagem(id_remetente, id_destinatario, datahora, texto)
        except Exception as e:
            print(e)

    @staticmethod
    def cria_de_tupla(self, dados):
        try:
            id = dados[0]
            id_remetente = dados[1]
            id_destinatario = dados[2]
            datahora = dados[3]
            texto = dados[4]
            return Mensagem(id_remetente, id_destinatario, datahora, texto, id=id)
        except Exception as e:
            print(e)
        


'''
{
"de": <int>,
"para": <int>,
"segredo": <str>,
"texto": <str>
}
Id da mensagem: int;
id do remetente: int;
id do destinatário: int; - pode ser 0, para indicar que a mensagem é visível a todos.
data/hora: str - use a biblioteca datetime para validar isso;
texto: str
'''