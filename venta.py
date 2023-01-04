from dueño import Dueño
class Venta(Dueño):
    nombreEmpresa = str
    dueño         = Dueño("","","","")
    
    def __init__(self, nombreEmpresa, dueño):
        self.nombreEmpresa = nombreEmpresa
        self.dueño = dueño