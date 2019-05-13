from modules.usuario import Usuario
import sqlite3

def listar():
    conexao = sqlite3.connect('chat.db')
    try:
        cursor = conexao.cursor()

        cursor.execute('select id, nome, segredo from Usuario')
        return [Usuario.cria_de_tupla(al) for al in cursor.fetchall()]
    except Exception as e:
        print(e)
    finally:
        conexao.close()

def buscar(id_usuario):
    conexao = sqlite3.connect('chat.db')
    try:
        cursor = conexao.cursor()

        cursor.execute('select id, nome, segredo from Usuario where id = ?', (id_usuario,))
        return Usuario.cria_de_tupla(cursor.fetchone())
    except Exception as e:
        print(e)
        return None
    finally:
        conexao.close()

def novo(usuario):
    conexao = sqlite3.connect('chat.db')
    try:
        cursor = conexao.cursor()

        cursor.execute('insert into Usuario (nome, segredo) values (:nome, :segredo)', usuario.__dict__())
        conexao.commit()
    except Exception as e:
        print(e)
    finally:
        conexao.close()
