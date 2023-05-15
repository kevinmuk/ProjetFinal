from pathlib import Path
import json
from datetime import *
class Personne:
    #definir le constructeur
    def __init__(self,nom:str="",prenom:str=""):
        self.set_nom(nom)
        self.set_prenom(prenom)

    #methodes d'accès
    def get_nom(self):
        return self.__nom
    def set_nom(self,value:str):
        self.__nom=value
    def get_prenom(self):
        return  self.__prenom
    def set_prenom(self,value:str):
        self.__prenom = value

class Employe(Personne):
    def __init__(self,nom:str="",prenom:str="", code:int=0, fonction:str=""):
        self.set_code(code)
        self.set_fonction(fonction)
        # appel du constructeur du parent
        super().__init__(nom, prenom)

    def get_code(self):
      return self.__code

    def set_code(self, value: int):
      self.__code = value

    def get_fonction(self):
      return self.__fonction

    def set_fonction(self, value: str):
      self.__fonction = value

class Client(Personne):
    def __init__(self, nom:str="",prenom:str="",telephone:str="",courriel:str=""):
        self.set_telephone(telephone)
        self.set_courriel(courriel)
        # appel du constructeur du parent
        super().__init__(nom, prenom)

    def get_telephone(self):
      return self.__telephone

    def set_telephone(self, value: str):
      self.__telephone = value

    def get_courriel(self):
      return self.__courriel

    def set_courriel(self, value: str):
      self.__courriel = value

class Reparation:
    def __init__(self, code : int = 0, description:str="", datereparation:datetime=None, montant:float=0.0, codeemploye:int=0):
        self.set_code(code)
        self.set_description(description)
        self.set_datereparation(datereparation)
        self.set_montant(montant)
        self.set_codeemploye(codeemploye)

    # méthodes d'accès
    def get_code(self):
        return self.__code

    def set_code(self, value:int):
        self.__code = value

    def get_description(self):
        return self.__description

    def set_description(self, value:str):
        self.__description = value

    def get_datereparation(self):
        return self.__datereparation

    def set_datereparation(self, value:datetime):
        self.__datereparation = value

    def get_montant(self):
        return self.__montant

    def set_montant(self, value:float):
        self.__montant = value

    def get_codeemploye(self):
        return self.__codeemploye

    def set_codeemploye(self, value:int):
        self.__codeemploye = value

class Voiture:
    def __init__(self, numeroplaque: str="", marque : str = "", modele: str="", couleur : str = "",  anne: int=0, proprietaire = Client):
        self.__numeroplaque = numeroplaque
        self.__marque = marque
        self.__modele = modele
        self.__couleur = couleur
        self.__anne = anne
        self.__proprietaire = proprietaire

    def get_numeroplaque(self):
        return self.__numeroplaque

    def set_numeroplaque(self, value: str):
        self.__numeroplaque = value

    def get_marque(self) -> str:
        return self.__marque

    def set_marque(self, value: str):
        self.__marque = value

    def get_modele(self) -> str:
        return self.__modele

    def set_modele(self, value: str):
        self.__modele = value

    def get_couleur(self) -> str:
        return self.__couleur

    def set_couleur(self, value: str):
        self.__couleur = value

    def get_anne(self):
        return self.__anne

    def set_anne(self, value: int):
        self.__anne = value

    def get_proprietaire(self):
        return self.__proprietaire

    def set_proprietaire(self, value: str):
        self.__proprietaire = value

class Garage:
    #definir le constructeur
    def __init__(self,nom:str="",telephone:str="",adresse:str=""):
        self.set_nom(nom)
        self.set_telephone(telephone)
        self.set_adresse(adresse)

    #methodes d'accès
    def get_nom(self):
        return self.__nom
    def set_nom(self,value:str):
        self.__nom=value
    def get_telephone(self):
        return  self.__telephone
    def set_telephone(self,value:str):
        self.__telephone = value
    def get_adresse(self):
        return self.__adresse
    def set_adresse(self,value:str):
        self.__adresse=value
