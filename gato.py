from reino_animal import Animal

class Gato(Animal): 
    def __init__(self, nombre: str, edad: int, colorDePelaje: str):
        super().__init__(nombre, edad)
        self.__colorDePelaje= colorDePelaje
    
    def _hablar(self):
        return f"Miau"

   