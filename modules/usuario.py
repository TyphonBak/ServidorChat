class Usuario:
    def __init__(self, nome, segredo=None, id=0):
        self.id = id
        self.nome = nome
        self.segredo = segredo

    def __dict__(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "segredo": self.segredo
        }

    @staticmethod
    def cria(dados):
        try:
            nome = dados["nome"]    
            segredo = dados["segredo"]
            return Usuario(nome, segredo=segredo)
        except Exception as e:
            print(e)
            return e

    @staticmethod
    def cria_de_tupla(dados):
        try:
            id = dados[0]
            nome = dados[1]
            return Usuario(nome, id=id), None
        except TypeError as te:
            return None, 'Usuario não encontrado'
        except Exception as e:
            print(e)
            return None, e
