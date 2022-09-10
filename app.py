# Importando as bibliotecas necessárias

from flask import Flask, render_template, request, url_for, redirect 
from flask_sqlalchemy import SQLAlchemy

# Instanciando o Flask
app = Flask(__name__, template_folder='templates') # App recebe o Flask e o template_folder é o caminho para a pasta onde estão os templates
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.sqlite3' # Definindo o caminho para o banco de dados

db = SQLAlchemy(app) # Instanciando o SQLAlchemy

# Criando a classe Produto, aqui é onde definimos os atributos da tabela
class Produto(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    valor = db.Column(db.Integer)
    marca = db.Column(db.String(150))
    ano = db.Column(db.Integer)

    # Assim como aprendemos em aula, o método __init__ é o construtor da classe, ele é chamado quando instanciamos um  ou mais objetos
    def __init__(self, nome, valor, marca, ano):
        self.nome = nome
        self.valor = valor
        self.marca = marca
        self.ano = ano

# Criando a rota para a página inicial
@app.route('/')
def index(): # Função que renderiza a página inicial
    carros = Produto.query.all()
    return render_template('index.html', estudantes=carros) # Estudantes é uma variável que será usada no template



# Criando a rota para a página de cadastro
@app.route('/add', methods=['GET', 'POST']) # Método GET para renderizar a página e o POST para receber os dados do formulário
def add():
    if request.method == 'POST':
        car_add = Produto(request.form['nome'], request.form['valor'], request.form['marca'], request.form['ano'])
        db.session.add(car_add) # Adicionando o objeto car_add ao banco de dados
        db.session.commit() # Salvando as alterações

        # se a resposta for vazia, exclui o objeto
        if request.form['nome'] == '':
            db.session.delete(car_add)
            db.session.commit()
            
        return redirect(url_for('index')) # Redirecionando para a página inicial
    return render_template('add.html') # Renderizando a página de cadastro


@app.route('/edit/<int:id>', methods=['GET', 'POST']) # Método GET para renderizar a página e o POST para receber os dados do formulário
def edit(id):

    car_edit = Produto.query.get(id) # Pegando o objeto com o id passado na rota
    # Verificando se o método é POST
    if request.method == 'POST':
        car_edit.nome = request.form['nome']
        car_edit.valor = request.form['valor']
        car_edit.marca = request.form['marca']
        car_edit.ano = request.form['ano']
        db.session.commit() # Salvando as alterações
        return redirect(url_for('index')) # Redirecionando para a página inicial
    return render_template('edit.html', estudante=car_edit)


@app.route('/delete/<int:id>')
def delete(id):
    car_delete = Produto.query.get(id) # Pegando o objeto com o id passado na rota
    db.session.delete(car_delete) # Deletando o objeto
    db.session.commit() # Salvando as alterações
    return redirect(url_for('index')) # Redirecionando para a página inicial

if __name__ == '__main__':
    db.create_all() # Criando as tabelas
    app.run(debug=True) # Executando o Flask