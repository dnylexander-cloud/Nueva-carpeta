from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "daniel12"  # cambia esto por algo más fuerte después

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="sistema_login",
        user="postgres",
        password="daniel11"
    )
    return conn


# Página principal
@app.route('/')
def home():
    return redirect(url_for('login'))


# Registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        conn = get_db_connection()
        cur = conn.cursor()

        try:
            cur.execute(
                "INSERT INTO usuarios (username, password) VALUES (%s, %s)",
                (username, password)
            )
            conn.commit()
        except Exception as e:
            conn.rollback()
            cur.close()
            conn.close()
            return f"Error: {e} - El usuario puede existir"

        cur.close()
        conn.close()

        return redirect(url_for('login'))

    return render_template('registro.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
        user = cur.fetchone()

        cur.close()
        conn.close()

        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect(url_for('bienvenida'))
        else:
            return "Usuario o contraseña incorrectos"

    return render_template('login.html')


# Bienvenida
@app.route('/bienvenida')
def bienvenida():
    if 'username' in session:
        return render_template('bienvenida.html')
    else:
        return redirect(url_for('login'))


# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)