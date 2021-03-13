import sqlite3
import os
from flask import Flask, g, render_template
from DBase import DBase
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




@app.route('/login', methods=["POST","GET"])
def login():
    return render_template("login.html")

@app.route('/register', methods=["POST","GET"])
    db = get_db()
    dbase = DBase(db)
    if request.method == "POST":
        


if __name__ == "__main__":
    app.run(debug=True)
