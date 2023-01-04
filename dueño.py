from comprador import Comprador
from marca import Marca

class Dueño(Marca):
    nombre    = str
    apellido  = str
    marca     = Marca("", "", "")
    comprador = Comprador("","","")
    
    def __init__(self, nombre, apellido, marca, comprador):
        self.nombre    = nombre
        self.apellido  = apellido
        self.marca     = marca
        self.comprador = comprador