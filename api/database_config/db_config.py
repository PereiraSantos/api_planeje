import sqlite3
from flask import Flask
import json

def open_config():
    with open("config.json") as json_file:
        json_data = json.load(json_file)
    return json_data['url']

def get_db():
    db = sqlite3.connect(open_config())
    db.row_factory = sqlite3.Row
    return db

def init_db(app: Flask):
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()