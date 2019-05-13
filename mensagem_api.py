from flask import Blueprint, request, jsonify
from services.mensagem_service import nova as service_nova

mensagem_app = Blueprint('mensagem_app', __name__)

@mensagem_app.route('/msg', methods=['POST'])
def nova():
    res = request.get_json()
    service_nova(res)

@mensagem_app.route('/msg/<int:id_usuario>', methods=['GET'])
def listar_por_usuario(id_usuario):
    print(request.args)
    return jsonify('Show')