from database_config import db_config
from flask import Request, jsonify
import sqlite3

def home():
    return """
    <h1>Bem-vindo à API CRUD com Flask</h1>
    <p>Esta API permite que você execute operações CRUD (Create, Read, Update, Delete) em uma base de dados SQLite.</p>
    <p>Rotas disponíveis:</p>
    <ul>
        <li>POST /dados - Adiciona um novo dado. Envie um JSON com os campos 'nome' e 'idade'.</li>
        <li>GET /dados - Retorna todos os dados na base de dados.</li>
        <li>GET /dados/{id} - Retorna um dado específico por ID.</li>
        <li>PUT /dados/{id} - Atualiza um dado existente por ID. Envie um JSON com os campos 'nome' e 'idade'.</li>
        <li>DELETE /dados/{id} - Deleta um dado existente por ID.</li>
    </ul>
    """

def manage_dados(request: Request):
    if request.method == 'POST':
        password = request.json.get('password')
        login = request.json.get('login')

        if not password or not login:
            return jsonify({'error': 'password e login são obrigatórios'}), 400

        try:
            db = db_config.get_db()
            cursor = db.cursor()
            cursor.execute('INSERT INTO user (password, login) VALUES (?, ?)', (password, login))
            db.commit()
            return jsonify({'message': 'Dado gravado com sucesso!'}), 201
        except sqlite3.Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            db.close()
    elif request.method == 'GET':
        return home()

def get_dados():
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM user')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def get_dado_id(dado_id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM user WHERE id = ?', (dado_id,))
        dado = cursor.fetchone()
        if dado:
            return jsonify(dict(dado))
        else:
            return jsonify({'error': 'Dado não encontrado'}), 404
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()


def update_dado(request: Request):
    password = request.json.get('password')
    login = request.json.get('login')
    id = request.json.get('id')

    if not password or not login:
        return jsonify({'error': 'password e login são obrigatórios'}), 400

    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE user SET password = ?, login = ? WHERE id = ?', (password, login, id))
        db.commit()
        return jsonify({'message': 'Dado atualizado com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_dado(dado_id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM user WHERE id = ?', (dado_id,))
        db.commit()
        return jsonify({'message': 'Dado deletado com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def create_tables():
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS `user` (`id` INTEGER NOT NULL, `login` TEXT NOT NULL, `password` TEXT NOT NULL, `keep_logged` INTEGER NOT NULL, PRIMARY KEY (`id`))')
        db.commit()
        return jsonify({'message': 'tabela criada com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def register_user(request: Request):
    if request.method == 'POST':
        password = request.json.get('password')
        login = request.json.get('login')

        if not password or not login:
            return jsonify({'error': 'password e login são obrigatórios'}), 400

        try:
            db = db_config.get_db()
            cursor = db.cursor()
            cursor.execute('INSERT INTO user (password, login) VALUES (?, ?)', (password, login))
            db.commit()
            return jsonify({'message': 'Dado gravado com sucesso!'}), 201
        except sqlite3.Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            db.close()
    elif request.method == 'GET':
        return home()
    
def auth(request: Request):
    password = request.json.get('password')
    login = request.json.get('login')

    if not password or not login:
        return jsonify({'error': 'password e login são obrigatórios'}), 400

    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('select * from user WHERE password = ? and login = ?', (password, login))
        db.commit()
        return jsonify({'token': 'jkeedbewbwbfb weifd'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()