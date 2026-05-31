from reino_animal import Animal

class Pollo(Animal):
    def __init__ (self, nombre: str, edad: int, tipoPlumaje: str):
        super().__init__(nombre, edad)
        self.__tipoPlumaje= tipoPlumaje
        
    def _hablar (self): 
        return f"Pio"
    
    def poner_huevo (self):
        return f"El Pollo esta poniendo un huevo... "
    
    
    