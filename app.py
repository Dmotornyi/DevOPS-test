import sqlite3
import os
from flask import Flask, g, render_template, redirect, url_for, request
from flask_login import login_user, LoginManager, login_required, logout_user
from DBase import DBase
from werkzeug.security import generate_password_hash, check_password_hash
from UserLogin import  UserLogin
DATABASE = '/Users/dmotornyi/PycharmProjects/DevOPS-test/project.db'
SECRET_KEY = 'janfljsdnfjlasndfljnsalfgkmdksmglvdafngjlstghwet'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'project.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db



@app.route('/')
@app.route('/login', methods=["POST","GET"])
def login():
    db = get_db()
    dbase = DBase(db)
    if request.method == ["POST"]:
        user = dbase.getUser(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect('???')
    return render_template("login.html")

@app.route('/register', methods=["POST","GET"])
def register():
    db = get_db()
    dbase = DBase(db)
    if request.method == "POST":
        if len(request.form['name']) > 3 and len(request.form['psw']) > 3:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'], hash)
    return render_template("register.html")




if __name__ == "__main__":
    app.run(debug=True)
