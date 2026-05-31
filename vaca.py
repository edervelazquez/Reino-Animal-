from reino_animal import Animal
class Vaca(Animal):
    def __init__ (self, nombre: str, edad: int, litrosLeche: float):
        super().__init__(nombre, edad)
        self.__litrosLeche= litrosLeche
    
    def _hablar(self):
        return f"Muuu"
    
    def produccionDelDia (self):
        return f"La vaca produjo el dia de hoy {self.__litrosLeche} L de leche"
 