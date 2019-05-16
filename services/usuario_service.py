from modules.usuario import Usuario
from infra.usuario_db import listar as lista_db, buscar as buscar_db, novo as novo_db
from services.gen_secret import gera_segredo
import requests as req


def listar():
    return lista_db()

def buscar(id_user, dados):
    usuario, erro = buscar_db(id_user, dados.get('segredo'))
    if erro:
        erro = {'title': erro, 'status': 404}
    return usuario, erro

def novo(dados):
    try:
        if dados['nome'] in [us.nome for us in listar()]:
            return None, {'status': 409 ,'title': 'Usuario ja existente'}

        if verifica_nome_lms(dados["nome"]):
            dados['segredo'] = gera_segredo()
            usuario = Usuario.cria(dados)
            if usuario:
                novo_db(usuario)
                usuario = listar()[-1]
                return {"id": usuario.id, "segredo": dados['segredo']}, None
    except Exception as e:
        print(e)        
    return None, {'status': 400 ,'title': 'Nao autorizado. Apenas usuarios cadastrados no LMS podem se cadastrar.'}

def verifica_nome_lms(nome):
    alunos = req.get('http://localhost:5000/alunos').json()
    aluno_valido = list(filter(lambda al: al["nome"] == nome, alunos))
    
    if len(aluno_valido):
        return True
    
    professores = req.get('http://localhost:5000/professores').json()
    prof_valido = list(filter(lambda pr: pr["nome"] == nome, professores))
    if len(prof_valido):
        return True

    return False
