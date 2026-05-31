from reino_animal import Animal
from gato import Gato
from pollo import Pollo
from vaca import Vaca 

def main():
    print ("--INSTANCIAS DEL REINO ANIMAL--")
    
    print ("---METODOS DE GATO")
    gato_1= Gato ("Gato", 10, "Negro")
    print(gato_1._hablar())
    print(gato_1.obtenerDatos()) 
    
    print ("---METODOS DE POLLO")
    pollo_1= Pollo ("Pollo", 2, "Tricolor")
    print(pollo_1._hablar())
    print(pollo_1.obtenerDatos()) 
    print(pollo_1.poner_huevo())
    
    print ("---METODOS DE VACA--")
    vaca_1= Vaca ("Vaca,", 3, 25)
    print(vaca_1._hablar())
    print(vaca_1.obtenerDatos())
    print(vaca_1.produccionDelDia())
    
if __name__ == "__main__":
    main() 
        
    
    
    