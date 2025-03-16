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

def insert_annotation(request: Request):
    if request.method == 'POST':
        title = request.json.get('title')
        text = request.json.get('text')
        dateText = request.json.get('dateText')
        idRevision = request.json.get('idRevision')
       
        if not title or not text or not dateText or not idRevision:
            return jsonify({'error': 'title e description são obrigatórios'}), 400

        try:
            db = db_config.get_db()
            cursor = db.cursor()
            cursor.execute('INSERT INTO annotation (title, text, date_text, id_revision) VALUES (?, ?, ?, ? )', (title, text, dateText, idRevision))
            db.commit()
            return jsonify({'message': 'Dado gravado com sucesso!'}), 201
        except sqlite3.Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            db.close()
    elif request.method == 'GET':
        return home()

def get_annotation():
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM annotation')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def get_annotation_id(id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM annotation WHERE id = ?', (id,))
        dado = cursor.fetchone()
        if dado:
            return jsonify(dict(dado))
        else:
            return jsonify({'error': 'Dado não encontrado'}), 404
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()


def update_annotation(request: Request):
    id = request.json.get('id')
    title = request.json.get('title')
    text = request.json.get('text')
    dateText = request.json.get('dateText')
    idRevision = request.json.get('idRevision')

    if not title or not text or not dateText or not idRevision or not id:
        return jsonify({'error': 'title, description e id são obrigatórios'}), 400

    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE annotation SET title = ?, text = ? , date_text = ?, id_revision = ? WHERE id = ?', (title, text, dateText, idRevision, id))
        db.commit()
        return jsonify({'message': 'Dado atualizado com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_annotation(id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM annotation WHERE id = ?', (id,))
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
        cursor.execute('CREATE TABLE IF NOT EXISTS `annotation` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `title` TEXT, `text` TEXT, `date_text` TEXT, `id_revision` INTEGER)');

        db.commit()
        return jsonify({'message': 'tabela criada com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

