from flask import Blueprint, jsonify, request
from modules.usuario import Usuario
from services.usuario_service import listar as service_listar, novo as service_novo

usuario_app = Blueprint('usuario_app',__name__)

@usuario_app.route('/usr', methods=['POST'])
def registra():
    #should receive something like this: {"nome": <str>}
    #if ok should return something like this: {"id": <int>, "segredo": <str>}
    res = request.get_json()
    usuario, erro = service_novo(res)

    if erro:
        return jsonify(erro['title']), erro['status']
    
    if usuario:
        return jsonify(usuario), 201
    
    return jsonify('iii rapaz'), 404


@usuario_app.route('/usr', methods=['GET'])
def listar():
    return jsonify([us.__dict__() for us in service_listar()]), 200
