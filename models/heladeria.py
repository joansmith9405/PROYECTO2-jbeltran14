import models.funciones as funciones
from models.base import Base
from models.complemento import Complemento

class Heladeria:
    def __init__(self , nombre :str , lista_productos: list):
        self.__nombre = nombre
        self.__lista_productos = lista_productos
        self.__venta_del_dia = 0
        
    def get_nombre(self) -> str:
            return self.__nombre

    def get_venta_del_dia(self) -> float:
        return self.__venta_del_dia
    
    def producto_mas_rentable(self) -> str:
        return funciones.producto_mas_rentable(self.__lista_productos)
    
    def vender(self, nombre_producto: str) -> bool:
        resultado = False
        producto_vender = None
        for producto in self.__lista_productos:
            if producto.get_nombre() == nombre_producto:
                producto_vender = producto
        if producto_vender is not None:
            lista_ingredientes = producto_vender.get_lista_ingredientes()
            ingredientes_completos = True
            for ingrediente in lista_ingredientes:
                if isinstance(ingrediente, Base) and ingrediente.get_inventario() < 1:
                    ingredientes_completos = False
                    break
                if isinstance(ingrediente, Complemento) and ingrediente.get_inventario() < 0.2:
                    ingredientes_completos = False
                    break
            if ingredientes_completos:
                for ingrediente in lista_ingredientes:
                    if isinstance(ingrediente, Base) and ingrediente.get_inventario() >= 1:
                        ingrediente.set_inventario(ingrediente.get_inventario() - 1)
                    if isinstance(ingrediente, Complemento) and ingrediente.get_inventario() >= 0.2:
                        ingrediente.set_inventario(ingrediente.get_inventario() - 0.2)
                self.__venta_del_dia = self.__venta_del_dia + producto_vender.get_precio_publico()
                resultado = True
        return resultado