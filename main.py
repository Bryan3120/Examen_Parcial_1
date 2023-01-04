from auto import Auto
from marca import Marca
from dueño import Dueño
from comprador import Comprador
from venta import Venta

# HERENCIA SIMPLE DENTRO DEL MISMO ARCHIVO
class Cliente1:
    nombre   = str
    apellido = str
    edad     = int

    def __init__(self, nombre, apellido, edad):
       self.nombre   = nombre
       self.apellido = apellido
       self.edad     = edad
    
class Hijo1(Cliente1):
    ciudad   = str

    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad)
        self.ciudad   = ciudad

#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO __str__

class Cliente2:
    nombre   = str
    apellido = str
    edad     = int

    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
    
    def __str__(self):
        return f'Hola {self.nombre} {self.apellido}, su edad es {self.edad}'

        
#REALIZAR UNA HERENCIA DENTRO DEL MISMO ARCHIVO DE UNA DE LAS CLASES CREADAS, 
#CREANDO UN METODO STR EN EL HIJO (IMPRMIR UN OBJETO CON ESA CLASE)
class Hijo2(Cliente2):
    ciudad   = str
    
    def __str__(self):
        return f'hola {self.nombre} {self.apellido}, tiene {self.edad} años y vive en la ciudad de {self.ciudad}'


class Cliente3:
    nombre   = str
    apellido = str
    edad     = int

    def __init__(self, nombre, apellido, edad):
       self.nombre   = nombre
       self.apellido = apellido
       self.edad     = edad
    
class Hijo3(Cliente3):
    ciudad = str

    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad)
        self.ciudad  = ciudad


#REALIZAR UNA HERENCIA QUE CONTENGA: VARIOS OBJETOS (2), 
# OBJETOS DENTRO DE OBEJTOS (2) Y OBJETOS DENTRO DE OBJETOS DENTRO DE OBJETOS (2)
class Cliente4(Marca):
    nombre   = str
    apellido = str
    edad     = int
    ciudad   = str
    marca    = Marca("", "", "")

    def __init__(self, nombre, apellido, edad, ciudad, marca):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.ciudad   = ciudad
        self.marca    = marca
        
class Cliente5(Dueño):
    nombre   = str
    apellido = str
    comprador = Comprador("", "", "")
    marca    = Marca("", "", "")
    
    
    
    def __init__(self, nombre, apellido, marca, comprador):
        self.nombre   = nombre
        self.apellido = apellido
        self.comprador = comprador
        self.marca    = marca
        
class Cliente6(Venta):
    nombreEmpresa   = str
    dueño           = Dueño("", "", "", "")
    
    def __init__(self, nombreEmpresa, dueño):
        self.nombreEmpresa = nombreEmpresa
        self.dueño         = dueño
        
    
if __name__ == "__main__":
    
    compra1 = Hijo1('Bryan', 'Caicedo', 20, 'Quito')
    print(vars(compra1))
    
    compra2 = Hijo2('Bryan', 'Caicedo', 20)
    print(vars(compra2))
    
    compra3 = Hijo3('Juan', 'Mata', 20, 'Quito')
    print(vars(compra3))
    
    compra4 = Cliente4('Bryan', 'Caicedo', 20, 'Quito', Marca(
        'Chevrolet', 'Ecuador', Auto('Corsa', 'Gris', 2022)))
    print(vars(compra4))
    print(vars(compra4.marca))
    print(vars(compra4.marca.auto))
    
    compra5 = Cliente5('Luis', 'Caizatoa', Marca('Chevrolet', 'Ecuador', Auto('Corsa', 'Gris', 2022)), 
                       Comprador('Bryan', 'Caicedo', 20000))
    print(vars(compra5))
    print(vars(compra5.marca))
    print(vars(compra5.marca.auto))
    print(vars(compra5.marca.auto))
    
    total = Cliente6('Chevrolet', Dueño('Luis', 'Caizatoa', Marca('Chevrolet', 'Ecuador', 
                    Auto('Corsa', 'Gris', 2022)),Comprador('Bryan', 'Caicedo', 200000)))
    print(vars(total))
    print(vars(total.dueño))
    print(vars(total.dueño.marca.auto))