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

def insert_revision_quiz(request: Request):
    if request.method == 'POST':
        dateRevision = request.json.get('date_revision')
        answer = request.json.get('answer')
        idQuiz = request.json.get('id_quiz')

        if not idQuiz or not dateRevision or not answer:
            return jsonify({'error': 'topic, dateRevision e answer são obrigatórios'}), 400

        try:
            db = db_config.get_db()
            cursor = db.cursor()
            cursor.execute('INSERT INTO revision_quiz (date_revision, answer, id_quiz) VALUES (?, ?, ?)', (dateRevision, answer, idQuiz))
            db.commit()
            return jsonify({'message': 'Dado gravado com sucesso!'}), 201
        except sqlite3.Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            db.close()
    elif request.method == 'GET':
        return home()

def get_revision_quiz():
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM revision_quiz')
        dados = cursor.fetchall()
        return jsonify([dict(row) for row in dados])
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def get_revision_quiz_id(id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM revision_quiz WHERE id = ?', (id,))
        dado = cursor.fetchone()
        if dado:
            return jsonify(dict(dado))
        else:
            return jsonify({'error': 'Dado não encontrado'}), 404
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()


def update_revision_quiz(request: Request):
    id = request.json.get('id')
    dateRevision = request.json.get('date_revision')
    answer = request.json.get('answer')
    idQuiz = request.json.get('id_quiz')

    if not idQuiz or not dateRevision or not id:
        return jsonify({'error': 'topic, description, answer e id são obrigatórios'}), 400

    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('UPDATE revision_quiz SET date_revision = ?, answer = ?, id_quiz = ? WHERE id = ?', (dateRevision, answer, idQuiz, id))
        db.commit()
        return jsonify({'message': 'Dado atualizado com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

def delete_revision_quiz(id):
    try:
        db = db_config.get_db()
        cursor = db.cursor()
        cursor.execute('DELETE FROM revision_quiz  WHERE id = ?', (id,))
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
        cursor.execute('CREATE TABLE IF NOT EXISTS `revision_quiz` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `date_revision` TEXT, `answer` INTEGER, `id_quiz` INTEGER)');

        db.commit()
        return jsonify({'message': 'tabela criada com sucesso!'})
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

