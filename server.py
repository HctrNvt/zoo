from flask import Flask,render_template
from random import Random
from animaux import Animal
import mysql.connector
# Il faut avoir les accès suivant sur la base de données
base = mysql.connector.connect(
    host = "localhost",
    user="root",
    database="zoo"
    )
app = Flask(__name__)
# {{ url_for('home') }}
@app.route('/')
def home():
    return render_template("Menu.html")

@app.route("/connexion/")
def index():
    return render_template("Connexion.html")

@app.route("/animaux/")
def animaux():
    return render_template("AjoutAnimaux.html")

@app.route("/utilisateurs/")
def utilisateurs():
    return render_template("AjoutUtilisateur.html")

phrase = ["Quel est votre nom de famille ?",
          "Quel est le nom de votre père ?",
          "Quel était le surnom de votre meilleur ami d'enfance ?",
          "Dans quelle ville vos parents se sont-ils rencontrés ?",
          """Combien d’animaux de compagnie aviez-vous à l’âge de 10 ans ?""",
          """Comment s’appelait votre instituteur préféré ?""",
          "Quel est votre film préféré ?"]

# Si on change le nombre de questions de sécurité différente, le système ne fonctionne pas
def choixQuestion(idUser:int):
    random = Random(idUser)
    return random.choice(phrase)

def ajoutAnimal(animal:Animal):
    infos = animal.getInfos()
    requete = "INSERT INTO Animal (idAnimal,nomAnimal,dateNaissance,dateArrivee) VALUES ("
    for i in infos:
        requete = requete + i+","
    requete += ")"
    cursor = base.cursor()
    cursor.execute(requete)
    base.commit()
    
if __name__ == '__main__':
    app.run()
