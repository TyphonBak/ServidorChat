from services.usuario_service import buscar as busca_usuario
from modules.mensagem import Mensagem
from infra.mensagem_db import novo as novo_db, buscar as buscar_db, listar as listar_db
from datetime import datetime

def monta_mensagem(dados):
    mensagem = {}
    try:
        mensagem['id_remetente'] = dados['de']
        mensagem['id_destinatario'] = dados['para']
        mensagem['datahora'] = datetime.now()
        mensagem['texto'] = dados['texto']
    except:
        mensagem = None
    return mensagem

def listar():
    return listar_db()

def listar_por_usuario(id_usuario, info):
    usuario = busca_usuario(id_usuario)
    if usuario and usuario.segredo == info.get('segredo'):
        pass
    return ''

def nova(dados):
    destinatario = True if busca_usuario(dados['para']) or dados['para']==0 else False
    usuario = busca_usuario(dados['de'])
    if not destinatario or not usuario:
        return None, {'status': 404, 'title': 'Referencia(s) inexistente(s)'}
    if usuario.segredo != dados['segredo']:
        return None, {'status': 403, 'title': 'Senha inválida'}

    mensagem_estruturada = monta_mensagem(dados)
    mensagem = Mensagem.cria(mensagem_estruturada)
    if mensagem:
        novo_db(mensagem)
        mensagem = listar()[-1]
        return {"id": mensagem.id, "datahora": mensagem.datahora}, None

    return None, {'status': 400 ,'title': 'Falha'} 

