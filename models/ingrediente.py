from abc import ABC, abstractmethod
import models.funciones as funciones

class Ingrediente(ABC):
    def __init__(self, nombre: str, precio:float, num_calorias: int, inventario: int, es_vegetariano:bool):
        self.__nombre = nombre
        self.__precio = precio
        self.__num_calorias = num_calorias
        self.__inventario = inventario
        self.__es_vegetariano = es_vegetariano


    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio

    def get_num_calorias(self):
        return self.__num_calorias
    
    def get_inventario(self):
        return self.__inventario
    
    def get_es_vegetariano(self):
        return self.__es_vegetariano
    
    
    def set_nombre(self , nombre :str):
        self.__nombre = nombre
    
    def set_precio(self , precio :float):
        self.__precio = precio

    def set_num_calorias(self, num_calorias :int):
        self.__num_calorias = num_calorias
    
    def set_inventario(self , inventario : int):
        self.__inventario = inventario
    
    def set_es_vegetariano(self, es_vegetariano : bool):
        self.__es_vegetariano = es_vegetariano
    


    @abstractmethod
    def abastecer(self):
     pass
 
    def es_sano(self) -> bool:
        return funciones.es_sano(self._num_calorias, self._es_vegetariano)


    
    
    
    



