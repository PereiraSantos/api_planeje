from database_config import db_config
from flask import Request, jsonify
import sqlite3


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

def insert_question(request: Request):
    if request.method == 'POST':
        idQuiz = request.json.get('idQuiz')
        description = request.json.get('description')
        answer = request.json.get('answer')

        if not idQuiz or not description or not answer:
            return jsonify({'error': 'topic, description  e answer são obrigatórios'}), 400

        try:
            db = db_config.get_db()
            cursor = db.cursor()
            cursor.execute('INSERT INTO question (id_quiz, description, answer) VALUES (?, ?, ?)', (idQuiz, description, answer))
            db.commit()
            return jsonify({'message': 'Dado gravado com sucesso!'}), 201
        except sqlite3.Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            db.close()
    elif request.method == 'GET':
        return home()

def get_question():
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM question')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def get_question_id(id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM question WHERE id = ?', (id,))
        dado = cursor.fetchone()
        if dado:
            return jsonify(dict(dado))
        else:
            return jsonify({'error': 'Dado não encontrado'}), 404
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()


def update_question(request: Request):
    id = request.json.get('id')
    idQuiz = request.json.get('idQuiz')
    description = request.json.get('description')
    answer = request.json.get('answer')

    if not idQuiz or not description or not id:
        return jsonify({'error': 'topic, description, answer e id são obrigatórios'}), 400

    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE question SET idQuiz = ?, descrriptiopn = ?, answer = ? WHERE id = ?', (idQuiz, description, answer,id))
        db.commit()
        return jsonify({'message': 'Dado atualizado com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_question(id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM question  WHERE id = ?', (id,))
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
        cursor.execute('CREATE TABLE IF NOT EXISTS `question` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `id_quiz` INTEGER, `description` TEXT, `answer` INTEGER)');

        db.commit()
        return jsonify({'message': 'tabela criada com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

