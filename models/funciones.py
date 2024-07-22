#Punto 1 | ¿Esto es Sano?

def ingrediente_es_sano(calorias:int,vegetariano:str) -> bool:
    if calorias < 100 or vegetariano:
        return True
    else:
        return False

#Punto 2 | Las Calorías
def conteo_calorias(lista_calorias) -> int :
    total_calorias = sum(lista_calorias)
    total_calorias *= 0.95
    total_calorias = round(total_calorias, 2)
    return total_calorias


#punto 3 | Costo
def calcular_costo(ingredientes : list) -> float:
    costo = 0
    for ingrediente in ingredientes:
        costo = costo + float(ingrediente.get_precio())
    return costo



#Punto 4 | Rentabilidad 
def calcular_rentabilidad(costo:int, ingredientes : list ) -> float :
    return costo - calcular_costo(ingredientes)
    
               
        
#El mejor producto
def producto_mas_rentable(datos_productos: list) -> str:
    lista_productos = []
    max_rentabilidad = max(datos_productos, key=lambda x: x.calcular_rentabilidad())
    for producto in datos_productos:
        if producto.calcular_rentabilidad() == max_rentabilidad.calcular_rentabilidad():
            lista_productos.append(producto.get_nombre())
    return str(lista_productos)
        