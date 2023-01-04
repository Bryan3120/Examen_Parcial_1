
class Comprador(object):
    nombre   = str
    apellido = str
    dinero   = int
    
    def __init__(self, nombre,apellido,dinero):
        self.nombre   = nombre
        self.apellido = apellido
        self.dinero   = dinero