from auto import Auto

class Marca(Auto):
    nombre = str
    pais   = str
    auto   = Auto("","","")
    
    def __init__(self, nombre, pais, auto):
        self.nombre = nombre
        self.pais   = pais
        self.auto   = auto