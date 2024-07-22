from models.ingrediente import Ingrediente

class Complemento(Ingrediente):
    def __init__(self, nombre: str, precio:float, num_calorias: int, inventario: int, es_vegetariano:bool, ):
        super().__init__(nombre, precio, num_calorias, inventario, es_vegetariano)
        self.__nombre = nombre
        self.__precio = precio
        self.__num_calorias = num_calorias
        self.__inventario = inventario
        self.__es_vegetariano = es_vegetariano

    def abastecer(self):
        pass
    
    def get_renovar_inventario(self):
        self.set_inventario(self.get_inventario() + 10)
    