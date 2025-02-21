from flask import Flask, request
from database_config import db_config
from routes import route_planeje

app = Flask(__name__)

@app.route('/')
def home():
    return route_planeje.home()

@app.route('/initdb')
def initialize_database():
    db_config.init_db(app=app)
    return 'Database initialized'

@app.route('/dados', methods=['POST'])
def manage_dados():
        return route_planeje.manage_dados(request=request)

@app.route('/dados', methods=['GET'])
def get_dados():
    return route_planeje.get_dados()

@app.route('/dados/<int:dado_id>', methods=['GET'])
def get_dado_id(dado_id):
    return route_planeje.get_dado_id(dado_id=dado_id)

@app.route('/dados', methods=['PUT'])
def update_dado():
    return route_planeje.update_dado(request=request)

@app.route('/dados/<int:dado_id>', methods=['DELETE'])
def delete_dado(dado_id):
    return route_planeje.delete_dado(dado_id=dado_id)

if __name__ == '__main__':
    app.run(debug=True)
