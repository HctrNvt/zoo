class Animal:
    def __init__(self,nomAnimal,dateNaissance,dateArrivee,dateDepart):
        self.infos = [nomAnimal,dateNaissance,dateArrivee,dateDepart]
    def getInfos(self):
        return self.infos

class Soigneur:
    def __init__(self,nom,prenom,grade:int):
        self.infos = [nom,prenom,grade]
    def getInfos(self):
        return self.infos
    
class Grade:
    def __init__(self,nom,niveau):
        self.infos = [nom,niveau]
    def getInfos(self):
        return self.infos
