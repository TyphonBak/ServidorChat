from flask import Flask
from usuario_api import usuario_app
from mensagem_api import mensagem_app
import sqlite3

def create_app():
    app = Flask(__name__)
    app.register_blueprint(usuario_app)
    app.register_blueprint(mensagem_app)

    return app

def cria_db():
    conexao = sqlite3.connect('chat.db')
    cursor = conexao.cursor()
    cursor.execute(
        'create table IF NOT EXISTS Usuario ( \
            id integer primary key autoincrement, \
            nome text not null, \
            segredo text not null \
        )'
    )
    cursor.execute(
        'create table IF NOT EXISTS Mensagem ( \
            id integer primary key autoincrement, \
            id_remetente integer not null, \
            id_destinatario integer not null, \
            datahora text, \
            texto text, \
            FOREIGN KEY (id_remetente) REFERENCES Usuario(id), \
            FOREIGN KEY (id_destinatario) REFERENCES Usuario(id) \
        )'
    )
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    app = create_app()
    cria_db()

    app.run(debug=True, port=6000, host='localhost')