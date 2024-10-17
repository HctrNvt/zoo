import mysql.connector
from random import Random
from entite import Animal
class Base:
    def __init__(self):
        self.base = mysql.connector.connect({
                'user': 'root',
                'password': 'mdp',
                'host': 'localhost',
                'database': 'zoo'
            })
        self.cursor = self.base.cursor()

    # Ajoute un animal à la base de données, animal doit contenir l'objet Animal du fichier entite.py
    def ajoutAnimal(self,animal:Animal):
        infos = animal.getInfos()
        requete = "INSERT INTO Animal (NomAnimal,DateNaissance,DateArriveeZoo,DateDepartZoo) VALUES ("
        # On ajoute les informations chaque infos de animal à la suite de la requete
        for i in infos:
            requete = requete + i+","
        requete += ")"
        print(requete)
        self.cursor.execute(requete)
        self.base.commit()
    # Récupère l'enregistrement du soigneur lié à l'id donné
    def getUser(self,idUser:int):
        requete = "SELECT * FROM soigneur WHERE Id_soigneur = "+str(idUser)
        self.cursor = self.base.cursor(requete)        
        return self.cursor.fetchall()
    # Renvoie tous les enregistrements de la table animal
    def getAnimaux(self):
        requete = "SELECT * FROM animal"
        self.cursor = self.base.cursor(requete)
        return self.cursor.fetchall()
    # Renvoie la question personnalisé de l'utilisateur
    # Après avoir fait le premier ajout d'utilisateur, il ne faut plus modifier la quantité/contenus de phrase
    def getQuestionSecurite(self,idUser:int):  
        phrase = ["Quel est votre nom de famille ?",
                  "Quel est le nom de votre père ?",
                  "Quel était le surnom de votre meilleur ami d'enfance ?",
                  "Dans quelle ville vos parents se sont-ils rencontrés ?",
                  """Combien d’animaux de compagnie aviez-vous à l’âge de 10 ans ?""",
                  """Comment s’appelait votre instituteur préféré ?""",
                  "Quel est votre film préféré ?"]

        # Si on change le nombre de questions de sécurité différente, le système ne fonctionne pas
        random = Random(idUser)
        return random.choice(phrase)
