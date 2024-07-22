from models.iproducto import iProducto
import models.funciones as funciones

class Copa(iProducto):
    def __init__(self, nombre:str, precio_publico:float, tipo_vaso: str , lista_ingredientes : list):
       self.__nombre = nombre
       self.__precio_publico = precio_publico
       self.__tipo_vaso = tipo_vaso
       self.__lista_ingredientes = lista_ingredientes
       
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_precio_publico(self, precio_publico: float):
        self.__precio_publico = precio_publico

    def set_tipo_vaso(self, tipo_vaso: str):
        self.__tipo_vaso = tipo_vaso

    def set_lista_ingredientes(self, lista_ingredientes: list):
        self.__lista_ingredientes = lista_ingredientes
        
     
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_precio_publico(self) -> float:
        return self.__precio_publico

    def get_tipo_vaso(self) -> str:
        return self.__tipo_vaso

    def get_lista_ingredientes(self) -> list:
        return self.__lista_ingredientes    
    
    def calcular_costo(self) -> float :
        costo = funciones.calcular_costo(self.__lista_ingredientes)
        return costo
    
    def calcular_calorias(self) -> float:
        lista_calorias = []
        for ingrediente in self.__lista_ingredientes:
            lista_calorias.append(ingrediente.get_num_calorias())
        return funciones.conteo_calorias(lista_calorias)    
    
    
    def calcular_rentabilidad(self)-> float:
         return funciones.calcular_rentabilidad(self.get_precio_publico(), self.__lista_ingredientes)