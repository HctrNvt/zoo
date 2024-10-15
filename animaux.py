class Animal:
    def __init__(self,idAnimal,nomAnimal,dateNaissance,dateArrivee):
        self.infos = [idAnimal,nomAnimal,dateNaissance,dateArrivee]
    def getInfos(self):
        return self.infos
    