from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abc.123'
app.config['MYSQL_DB'] = 'juegorol'

mysql = MySQL(app)

@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form["nombre"])
        print(request.form["contraseña"])
        print(request.form["rol"])
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route("/usuario/<nombre>")
def paginaUsuario():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM juegorol.usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    "hola"
    return render_template("usuario.html")


@app.route('/usuarios')
def mostrar_usuarios():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM juegorol.usuarios")
    usuarios = cursor.fetchall()
    nusuarios = len(usuarios)
    cursor.close()
    return render_template('usuarios.html', usuarios=usuarios, nusuarios=nusuarios)

@app.route('/personajes')
def mostrar_personajes():
    conn = mysql.connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM juegorol.personajes")
    pj = cursor.fetchall()
    print(pj)
    cursor.close()
    return render_template('personajes.html', pj=pj)

if __name__ == '__main__':
    app.run(debug= True)