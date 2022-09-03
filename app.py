from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.sqlite3'

db = SQLAlchemy(app)


class Produto(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    valor = db.Column(db.Integer)
    marca = db.Column(db.String(150))
    ano = db.Column(db.Integer)

    def __init__(self, nome, valor, marca, ano):
        self.nome = nome
        self.valor = valor
        self.marca = marca
        self.ano = ano


@app.route('/')
def index():
    carros = Produto.query.all()
    return render_template('index.html', estudantes=carros)




@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        car_add = Produto(request.form['nome'], request.form['valor'], request.form['marca'], request.form['ano'])
        db.session.add(car_add)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    car_edit = Produto.query.get(id)
    if request.method == 'POST':
        car_edit.nome = request.form['nome']
        car_edit.valor = request.form['valor']
        car_edit.marca = request.form['marca']
        car_edit.ano = request.form['ano']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', estudante=car_edit)


@app.route('/delete/<int:id>')
def delete(id):
    car_delete = Produto.query.get(id)
    db.session.delete(car_delete)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)