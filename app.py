from flask import Flask, render_template, request, redirect, url_for, flash, jsonify # Aqui importamos as bibliotecas necessárias para o funcionamento do nosso app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates') # Aqui criamos o objeto app que será o nosso objeto principal
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///carros.sqlite3' # configuramos a conexão com o banco de dados

db = SQLAlchemy(app) # Aqui criamos o objeto db que será o nosso objeto de conexão com o banco de dados

class Carros(db.Model): # Aqui criamos a classe Carros que será responsável por armazenar os dados dos carros
    modelo = db.Column('modelo', db.Integer, primary_key=True, autoincrement=True)
    marca = db.column('marca', db.String(20))
    valor = db.column('valor', db.Float)

    def __init__(self, marca, valor): # Construtor da classe Carros
        self.marca = marca
        self.valor = valor

@app.route('/') # Aqui criamos a rota principal do nosso app
def index(): # Aqui criamos a função index que será responsável por renderizar a página principal do nosso app
    carros = Carros.query.all() # Aqui criamos uma variável carros que receberá todos os carros do banco de dados
    return render_template('index.html', carros=carros) # Chamamos a página

if __name__ == '__main__':
    db.create_all() # Criação do banco de dados
    app.run(debug=True) # Roda o app em modo debug
