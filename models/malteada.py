from models.iproducto import iProducto
import models.funciones as funciones

class Malteada:
    def __init__(self, nombre:str, precio_publico:float,  volumen: int, lista_ingredientes: list):
       #super().__init__(nombre, precio_publico)
        self.__nombre = nombre
        self.__precio_publico = precio_publico
        self.__volumen = volumen
        self.__lista_ingredientes = lista_ingredientes
       
    def set_nombre(self, nombre: str):
            self.__nombre = nombre

    def set_precio_publico(self, precio_publico: float):
        self.__precio_publico = precio_publico

    def set_volumen(self, volumen: int):
        self.__volumen = volumen

    def set_lista_ingredientes(self, lista_ingredientes: list):
        self.__lista_ingredientes = lista_ingredientes 
        
    def get_nombre(self) -> str:
            return self.__nombre

    def get_precio_publico(self) -> float:
        return self.__precio_publico

    def get_volumen(self) -> int:
        return self.__volumen

    def get_lista_ingredientes(self) -> list:
        return self.__lista_ingredientes    
       
    def get_tipo_vaso(self):
        return self._tipo_vaso
    
    def calcular_costo(self)-> float:
        return funciones.calcular_costo(self.__lista_ingredientes) + 500
    
    
    def calcular_calorias(self) -> float:
        lista_calorias = []
        for ingrediente in self.__lista_ingredientes:
            lista_calorias.append(ingrediente.get_num_calorias())
        return funciones.conteo_calorias(lista_calorias) + 200
    
    
    def calcular_rentabilidad(self):
        return funciones.calcular_rentabilidad(self.get_precio_publico(), self.__lista_ingredientes)

    
