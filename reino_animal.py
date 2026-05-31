from abc import ABC, abstractmethod 

class Animal (ABC): 
    def __init__ (self, nombre: str, edad: int): 
        self.__nombre= nombre 
        self.__edad= edad 

    @abstractmethod
    def _hablar (self):
        pass 
    def obtenerDatos(self): 
       return f"Es un {self.__nombre} y tiene {self.__edad} anios. "
    
    