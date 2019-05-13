from modules.usuario import Usuario
from infra.usuario_db import listar as lista_db, buscar as buscar_db
import requests as req


def listar():
    return lista_db()

def buscar(id_user):
    return buscar_db(id_user)

def novo(dados):
    try:
        if dados['nome'] in [us['nome'] for us in listar()]:
            return None, {'status': 409 ,'title': 'Usuario ja existente'}

        if verifica_nome_lms(dados["nome"]):
            #adicionar 'segredo' em dados aqui
            usuario = Usuario.cria(dados)
            if usuario:
                novo_db(usuario)
                usuario = listar()[-1]
                return {"id": usuario.id, "segredo": usuario.segredo}, None
    except Exception as e:
        print(e)        
    return None, {'status': 400 ,'title': 'Nao autorizado'}

def verifica_nome_lms(nome):
    alunos = req.get('localhost:5000/alunos')
    aluno_valido = list(filter(lambda al: al["nome"] == nome), alunos)
    
    if len(aluno_valido):
        return True
    
    professores = req.get('localhost:5000/professores')
    prof_valido = list(filter(lambda pr: pr["nome"] == nome), professores)
    if len(prof_valido):
        return True

    return False
