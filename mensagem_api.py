from flask import Blueprint, request, jsonify
from services.mensagem_service import nova as service_nova, listar as service_listar

mensagem_app = Blueprint('mensagem_app', __name__)

@mensagem_app.route('/msg', methods=['POST'])
def nova():
    res = request.get_json()
    service_nova(res)

@mensagem_app.route('/msg/<int:id_usuario>', methods=['GET'])
def listar_por_usuario(id_usuario):
    mensagens, erro = service_listar(id_usuario, request.args)
    if erro:
        return jsonify(erro['title']), erro['status']
    return jsonify({"mensagens": [msg.__dict__() for msg in mensagens]}), 200