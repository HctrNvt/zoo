import mysql.connector
from entite import Animal
class base:
    def __init__(self):
        self.base = mysql.connector.connection({
                'user': 'root',
                'password': 'mdp',
                'host': 'localhost',
                'database': 'zoo'
            })
        self.cursor = base.cursor()

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
        base.commit()
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