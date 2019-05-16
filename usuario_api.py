from flask import Blueprint, jsonify, request
from modules.usuario import Usuario
from services.usuario_service import listar as service_listar, novo as service_novo, buscar as service_buscar

usuario_app = Blueprint('usuario_app',__name__)

@usuario_app.route('/usr', methods=['POST'])
def registra():
    res = request.get_json()
    usuario, erro = service_novo(res)

    if erro:
        return jsonify(erro['title']), erro['status']    
    if usuario:
        return jsonify(usuario), 201    
    return jsonify('Algo inesperado ocorreu. Contate o suporte'), 404


@usuario_app.route('/usr', methods=['GET'])
def listar():
    return jsonify({"usr": [us.__dict__() for us in service_listar()]}), 200

@usuario_app.route('/usr/<int:id_usuario>', methods=['GET'])
def buscar(id_usuario):
    usuario, erro = service_buscar(id_usuario, request.args)
    if erro:
        return jsonify(erro['title']), erro['status']
    return jsonify(usuario.__dict__())
