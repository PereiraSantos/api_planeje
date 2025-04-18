from flask import Flask, request
from database_config import db_config
from routes import route_user, route_revision, route_revision_date, route_annotation, route_quiz, route_question, route_revision_quiz

app = Flask(__name__)

@app.route('/')
def home():
    return route_user.home()

@app.route('/initdb')
def initialize_database():
    db_config.init_db(app=app)
    return 'Database initialized'

# USER

@app.route('/dados', methods=['POST'])
def manage_dados():
    return route_user.manage_dados(request=request)

@app.route('/dados', methods=['GET'])
def get_dados():
    return route_user.get_dados()

@app.route('/dados/<int:dado_id>', methods=['GET'])
def get_dado_id(dado_id):
    return route_user.get_dado_id(dado_id=dado_id)

@app.route('/dados', methods=['PUT'])
def update_dado():
    return route_user.update_dado(request=request)

@app.route('/dados/<int:dado_id>', methods=['DELETE'])
def delete_dado(dado_id):
    return route_user.delete_dado(dado_id=dado_id)

@app.route('/dados/user/createtable', methods=['GET'])
def create_tables():
    return route_user.create_tables()

@app.route('/dados/register/user', methods=['POST'])
def register_user():
    return route_user.register_user(request=request)

@app.route('/dados/user/auth', methods=['POST'])
def auth_user():
    return route_user.auth(request=request)

# REVISION

@app.route('/revision/createtable', methods=['GET'])
def create_tables_revision():
    return route_revision.create_tables()

@app.route('/revision', methods=['POST'])
def post_revision():
    return route_revision.insert_revision(request=request)

@app.route('/revision', methods=['GET'])
def get_revision():
    return route_revision.get_revision()

@app.route('/revision/<int:id>', methods=['GET'])
def get_revision_id(id):
    return route_revision.get_revision_id(id=id)

@app.route('/revision/update', methods=['PUT'])
def update_revision():
    return route_revision.update_revision(request=request)

@app.route('/revision/delete/<int:id>', methods=['DELETE'])
def delete_revision(id):
    return route_revision.delete_revision(id=id)

# DATE REVISION

@app.route('/revision/date/createtable', methods=['GET'])
def create_tables_revision_date():
    return route_revision_date.create_tables()

@app.route('/revision/date', methods=['POST'])
def post_revision_date():
    return route_revision_date.insert_revision_date(request=request)

@app.route('/revision/date', methods=['GET'])
def get_revision_date():
    return route_revision_date.get_revision_date()

@app.route('/revision/date/<int:id>', methods=['GET'])
def get_revision_date_id(id):
    return route_revision_date.get_revision_date_id(id=id)

@app.route('/revision/date/update', methods=['PUT'])
def update_revision_date():
    return route_revision_date.update_revision_date(request=request)

@app.route('/revision/date/delete/<int:id>', methods=['DELETE'])
def delete_revision_date(id):
    return route_revision_date.delete_revision_date(id=id)

# ANNOTATION

@app.route('/annotation/createtable', methods=['GET'])
def create_tables_annotation():
    return route_annotation.create_tables()

@app.route('/annotation', methods=['POST'])
def post_annotation():
    return route_annotation.insert_annotation(request=request)

@app.route('/annotation', methods=['GET'])
def get_annotation():
    return route_annotation.get_annotation()

@app.route('/annotation/<int:id>', methods=['GET'])
def get_annotation_id(id):
    return route_annotation.get_annotation_id(id=id)

@app.route('/annotation/update', methods=['PUT'])
def update_annotation():
    return route_annotation.update_annotation(request=request)

@app.route('/annotation/delete/<int:id>', methods=['DELETE'])
def delete_annotation(id):
    return route_annotation.delete_annotation(id=id)

# QUIZ

@app.route('/quiz/createtable', methods=['GET'])
def create_tables_quiz():
    return route_quiz.create_tables()

@app.route('/quiz', methods=['POST'])
def post_quiz():
    return route_quiz.insert_quiz(request=request)

@app.route('/quiz', methods=['GET'])
def get_quiz():
    return route_quiz.get_quiz()

@app.route('/quiz/<int:id>', methods=['GET'])
def get_quiz_id(id):
    return route_quiz.get_quiz_id(id=id)

@app.route('/quiz/update', methods=['PUT'])
def update_quiz():
    return route_quiz.update_quiz(request=request)

@app.route('/quiz/delete/<int:id>', methods=['DELETE'])
def delete_quiz(id):
    return route_quiz.delete_quiz(id=id)

# QUESTION

@app.route('/question/createtable', methods=['GET'])
def create_tables_question():
    return route_question.create_tables()

@app.route('/question', methods=['POST'])
def post_question():
    return route_question.insert_question(request=request)

@app.route('/question', methods=['GET'])
def get_question():
    return route_question.get_question()

@app.route('/question/<int:id>', methods=['GET'])
def get_question_id(id):
    return route_question.get_question_id(id=id)

@app.route('/question/update', methods=['PUT'])
def update_question():
    return route_question.update_question(request=request)

@app.route('/question/delete/<int:id>', methods=['DELETE'])
def delete_question(id):
    return route_question.delete_question(id=id)

# REVISION QUIZ

@app.route('/revision/quiz/createtable', methods=['GET'])
def create_tables_revision_quiz():
    return route_revision_quiz.create_tables()

@app.route('/revision/quiz', methods=['POST'])
def post_revision_quiz():
    return route_revision_quiz.insert_revision_quiz(request=request)

@app.route('/revision/quiz', methods=['GET'])
def get_revision_quiz():
    return route_revision_quiz.get_revision_quiz()

@app.route('/revision/quiz/<int:id>', methods=['GET'])
def get_revision_quiz_id(id):
    return route_revision_quiz.get_revision_quiz_id(id=id)

@app.route('/revision/quiz/update', methods=['PUT'])
def update_revision_quiz():
    return route_revision_quiz.update_revision_quiz(request=request)

@app.route('/revision/quiz/delete/<int:id>', methods=['DELETE'])
def delete_revision_quiz(id):
    return route_revision_quiz.delete_revision_quiz(id=id)


if __name__ == '__main__':
    app.run(debug=True)
