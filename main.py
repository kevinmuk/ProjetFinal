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
        if value[0].isupper() and 6<=len(value)<=20:
          self.__nom = value
        else:
            raise ValueError("nom doit commencer par une majuscule et avoir la longueur de 6 a 20 lettres")
    def get_prenom(self):
        return  self.__prenom
    def set_prenom(self,value:str):
         if value[0].isupper() and 6<len(value)<20:
          self.__prenom = value
         else:
             raise ValueError("nom doit commencer par une majuscule et avoir la longueur de 6 a 20 lettres")

    def __str__(self)->str:
        return f"{self.get_nom()}\t{self.get_prenom()}\t"

class Employe(Personne):
    def __init__(self,nom:str="",prenom:str="", code:int=0, fonction:str=""):
        self.set_code(code)
        self.set_fonction(fonction)
        # appel du constructeur du parent
        super().__init__(nom, prenom)

    #methodes d'accès
    def get_code(self):
      return self.__code

    def set_code(self, value: int):
      self.__code = value

    def get_fonction(self):
      return self.__fonction

    def set_fonction(self, value: str):
      self.__fonction = value

    def __str__(self)->str:
        return f"{self.get_nom()}\t{self.get_prenom()}\t"\
            f"{self.get_code()}\t{self.get_fonction()}\t"


class Client(Personne):
    def __init__(self, nom:str="",prenom:str="",telephone:str="",courriel:str=""):
        self.set_telephone(telephone)
        self.set_courriel(courriel)
        # appel du constructeur du parent
        super().__init__(nom, prenom)

    #methodes d'accès
    def get_telephone(self):
      return self.__telephone

    def set_telephone(self, value: str):
      self.__telephone = value

    def get_courriel(self):
      return self.__courriel

    def set_courriel(self, value: str):
      self.__courriel = value

    def __str__(self)->str:
        return f"{self.get_nom()}\t{self.get_prenom()}\t"\
            f"{self.get_telephone()}\t{self.get_courriel()}\t"

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
        self.listeReparation=[]

    #methodes d'accès
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

    def get_listeReparation(self)->list[Reparation]:
        return self.__listeReparation
    def set_listeReparation(self,value:list[Reparation]):
        self.__listeReparation=value

    def ajouterreparation(self, element:Reparation)->None:
        self.listeReparation.append(element)



class Garage:
    #definir le constructeur
    def __init__(self,nom:str="",telephone:str="",adresse:str=""):
        self.set_nom(nom)
        self.set_telephone(telephone)
        self.set_adresse(adresse)
        self.listeEmploye=[]
        self.listeVoiture=[]

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

    @property
    def listeEmploye(self)->list[Employe]:
        return self.__listeEmploye

    @listeEmploye.setter
    def listeEmploye(self,value:list[Employe]):
        self.__listeEmploye=value

    @property
    def listeVoiture(self)->list[Voiture]:
        return self.__listeVoiture

    @listeVoiture.setter
    def listeVoiture(self,value:list[Voiture]):
        self.__listeVoiture=value
    @classmethod
    def converttolist(cls, valeur:object)->list:
        # creer une liste pour mettre les valeurs
        liste:list=[]
        for valeur in valeur.__dict__.values():
            liste.append(valeur)
        return liste

    @classmethod
    def createfromlist(cls,valeur:list[str])->object:
        garage:Garage=cls(int(valeur[0]),valeur[1],valeur[2])
        return garage

    @classmethod
    def createfromdict(cls,valeur:dict[str])->object:
        garage:Garage=Garage()
        for key,value in valeur.items():
            if key in garage.__dict__.keys():
                garage.__setattr__(key,value)
        return garage
     @classmethod
    def converttodict(cls, valeur:object)->dict:
        return valeur.__dict__
    def serialiser(self, valeurs:list[object])->None:
        #ouvrir le fichier (creer le stream)
        path:Path=Path(self.getchemin())
        stream=path.open('w')
        json.dump(valeurs,stream, indent=4,separators=(',',':'),default=Garage.converttodict)
        #fermer le stream
        stream.flush()
        stream.close()
    def deserialiser(self)->list[object]:
        #ouvrir le fichier (creer le stream)
        path:Path=Path(self.getchemin())
        stream=path.open('r')
        #deserialiser le fichier vers un objet liste de compte
        listegarage:list[Garage]=json.load(stream,object_hook=Garage.createfromdict)

        #fermer le stream
        stream.close()
        #retourner le resultat
        return listegarage



    def ajoutervoiture(self,element:Voiture)->None:
        self.listeVoiture.append(element)

    def getvoiture(self, numvoiture:str)->Voiture:
        for element in self.listeVoiture:
            if element.get_numeroplaque()==numvoiture:
              return element


    def ajouterreparation(self, numvoiture:str, reparation:Reparation)->None:
        for element in self.listeVoiture:
            if element.get_numeroplaque()==numvoiture:
                reparation = Voiture.get_listeReparation.append(reparation)
            else :
                raise ValueError
    def getreparation(self, numvoiture:str)->list[Reparation]:
        for element in self.listeVoiture:
            if element.get_numeroplaque()==numvoiture:
                return Voiture.get_listeReparation(Voiture)



