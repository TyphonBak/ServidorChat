class Usuario:
    def __init__(self, nome, segredo, id=0):
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
    def cria(self, dados):
        try:
            nome = dados["nome"]    
            segredo = dados["segredo"]
            return Usuario(nome, segredo)
        except Exception as e:
            print(e)
            return e

    @staticmethod
    def cria_de_tupla(self, dados):
        try:
            id = dados[0]
            nome = dados[1]
            segredo = dados[2]
            return Usuario(nome, segredo, id=id)
        except Exception as e:
            print(e)
            return e
