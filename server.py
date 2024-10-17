from flask import Flask,render_template
from requete import Base
# Il faut avoir les accès suivant sur la base de données

base = Base()

app = Flask(__name__)
# {{ url_for('home') }}
@app.route('/')
def home():
    return render_template("Menu.html")

@app.route("/login/")
def index():
    return render_template("Connexion.html")

@app.route("/animaux/")
def animaux():
    return render_template("AjoutAnimaux.html")

@app.route("/ajoutSoigneur/")
def utilisateurs():
    return render_template("AjoutSoigneur.html")

if __name__ == '__main__':
    app.run()
