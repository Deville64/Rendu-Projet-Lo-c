from flask import Flask, render_template, request
import mysql.connector as mariadb
app = Flask(__name__)
conn = mariadb.connect(
        user = 'root',
        password = 'root',
        database = 'Flask')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/page", methods=['POST'])
def page():
    name = request.form['name']
    lastname = request.form['lastname']
    pseudo = request.form['pseudo']
    sex = request.form['sex']

    cur = conn.cursor()
    cur.execute(f"INSERT INTO users (name, lastname, sex) VALUES ('{name}', '{lastname}', '{sex}')")
    conn.commit()

    return render_template("page.html", message = f"Bonjour {sex} {name} {lastname}, votre nom d'utilisateur est {pseudo}")

@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/info')
def info():
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return render_template("info.html", rows = rows)


if __name__ == "__main__":
    app.run()