from flask import Flask, render_template, request, redirect, url_for, flash
from flask.wrappers import Request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'C4p4d0c14'
app.config['MYSQL_DB'] = 'indicadores'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM manuales WHERE Proceso = "FORESTAL"')
    data = cur.fetchall()
    return render_template('indicadores.html', indicadores = data)

@app.route('/add_indicador', methods=['POST'])
def add_indicador():
    if request.method == 'POST':
        ind_name = request.form['ind_name']
        valor = request.form['valor']
        fecha = request.form['fecha']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO manuales (Indicador, Valor, Fecha) VALUES (%s, %s, %s)', [ind_name, valor, fecha])
        mysql.connection.commit()
        flash('Indicador Agregado') 
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_indicador():
    return 'edit indicador'

@app.route('/delete/<string:id>')
def delete_indicador(id):
    return id

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
