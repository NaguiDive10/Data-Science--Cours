##### 1 Classes ######
# %%
class Chien:
    pass

##### Objet  #####
# %%
mon_chien = Chien()
type(mon_chien)

#%%
### Attributs (données associées à l'objet)

class Chien:
    def __init__(self, nom, race):
        self.nom = nom  # Attribut d'instance
        self.race = race  # Attribut d'instance
        
#%%
mon_chien = Chien("Rex", "Labrador")
print(mon_chien.nom)
print(mon_chien.race)


# %%
### Méthodes (actions que l'objet peut effectuer)

class Chien:
    def __init__(self, nom, race):
        self.nom = nom  # Attribut d'instance
        self.race = race  # Attribut d'instance
        
    def aboyer(self):
        print(f"{self.nom} aboie !") # Méthode d'instance
#%%
rex = Chien("Rex", "Labrador") # Création d'une instance de Chien
rex.aboyer()  # Appel de la méthode aboyer

#################################################################################################
# %%### Héritage (création de classes dérivées)

class Calculator:
    def __init__(self,a,b):
        if not all(isinstance(x, (int, float)) for x in (a, b)):
            raise TypeError("Les deux arguments doivent être des entiers ou des flottants.")
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b
        
    def multiply(self):
        return self.a * self.b
        
calc = Calculator(3, 5)

#%%
print(calc.add())  # Affiche 8
print(calc.multiply())  # Affiche 15
# %%
