from database_config import db_config
from flask import Request, jsonify
import sqlite3
import datetime

def home():
    return """
    <p>Rotas disponíveis:</p>
    <ul>
        <li>POST /dados - Adiciona um novo dado. Envie um JSON com os campos 'nome' e 'idade'.</li>
        <li>GET /dados - Retorna todos os dados na base de dados.</li>
        <li>GET /dados/{id} - Retorna um dado específico por ID.</li>
        <li>PUT /dados/{id} - Atualiza um dado existente por ID. Envie um JSON com os campos 'nome' e 'idade'.</li>
        <li>DELETE /dados/{id} - Deleta um dado existente por ID.</li>
    </ul>
    """

def insert_revision(request: Request):
    if request.method == 'POST':
        title = request.json.get('title')
        description = request.json.get('description')
        dateCreational = datetime.datetime.now()

        if not title or not description or not dateCreational:
            return jsonify({'error': 'title e description são obrigatórios'}), 400

        try:
            db = db_config.get_db()
            cursor = db.cursor()
            cursor.execute('INSERT INTO revision (title, description, date_creational) VALUES (?, ?, ?)', (title, description, dateCreational))
            db.commit()
            return jsonify({'message': 'Dado gravado com sucesso!'}), 201
        except sqlite3.Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            db.close()
    elif request.method == 'GET':
        return home()

def get_revision():
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM revision')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def get_revision_id(id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM revision WHERE id = ?', (id,))
        dado = cursor.fetchone()
        if dado:
            return jsonify(dict(dado))
        else:
            return jsonify({'error': 'Dado não encontrado'}), 404
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()


def update_revision(request: Request):
    title = request.json.get('title')
    description = request.json.get('description')
    id = request.json.get('id')

    if not title or not description or not id:
        return jsonify({'error': 'title, description e id são obrigatórios'}), 400

    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE revision SET title = ?, description = ? WHERE id = ?', (title, description, id))
        db.commit()
        return jsonify({'message': 'Dado atualizado com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_revision(id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM revision WHERE id = ?', (id,))
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
        cursor.execute('CREATE TABLE IF NOT EXISTS `revision` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `title` TEXT, `description` TEXT, `date_creational` TEXT)')
        db.commit()
        return jsonify({'message': 'tabela criada com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

