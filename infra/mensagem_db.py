from modules.mensagem import Mensagem
import sqlite3

def listar():
    conexao = sqlite3.connect('chat.db')
    try:
        cursor = conexao.cursor()

        cursor.execute('select id, id_remetente, id_destinatario, datahora, texto from Mensagem')
        return [Mensagem.cria_de_tupla(al) for al in cursor.fetchall()]
    except Exception as e:
        print(e)
    finally:
        conexao.close()

def buscar(id_mensagem):
    conexao = sqlite3.connect('chat.db')
    try:
        cursor = conexao.cursor()

        cursor.execute('select id, id_remetente, id_destinatario, datahora, texto from Mensagem where id = ?', (id_mensagem,))
        return Mensagem.cria_de_tupla(cursor.fetchone())
    except Exception as e:
        print(e)
    finally:
        conexao.close()

def novo(mensagem):
    conexao = sqlite3.connect('chat.db')
    try:
        cursor = conexao.cursor()

        cursor.execute('insert into Mensagem (id_remetente, id_destinatario, datahora, texto) values (:id_remetente, :id_destinatario, :datahora, :texto)', mensagem.__dict__())
        conexao.commit()
    except Exception as e:
        print(e)
    finally:
        conexao.close()
