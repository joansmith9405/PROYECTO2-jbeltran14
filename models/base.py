from models.ingrediente import Ingrediente

class Base(Ingrediente):
    def __init__(self, nombre: str, precio:float, num_calorias: int, inventario: int, es_vegetariano:bool,sabor:str ):
        super().__init__(nombre, precio, num_calorias, inventario, es_vegetariano)
        self.__sabor = sabor
  
    def get_sabor(self):
        return self._sabor
    
    def set_sabor(self, sabor:str):
        self.__sabor = sabor

    def abastecer(self):
        self.set_inventario(self.get_inventario() + 5)
 