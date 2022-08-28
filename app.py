from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carros.sqlite3'

db = SQLAlchemy(app)

class Carros(db.Model):
    modelo = db.Column('modelo', db.Integer, primary_key=True, autoincrement=True)
    marca = db.column('marca', db.String(20))
    valor = db.column('valor', db.Float)

    def __init__(self, marca, valor):
        self.marca = marca
        self.valor = valor

@app.route('/')
def index():
    carros = Carros.query.all()
    return render_template('index.html', carros=carros)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
