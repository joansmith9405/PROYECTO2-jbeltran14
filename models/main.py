from models.base import Base
from models.complemento import Complemento
from models.copa import Copa
from models.malteada import Malteada
from models.heladeria import Heladeria

#Módulo que contiene las pruebas funcionales de crear una Heladeria, vender productos y obtener el mas rentable.
print("DEFINIR INGREDIENTES Y PRODUCTOS")


" lista de ingredientes Base"
fresa = Base("FRESITAS",2800,11,5,False,"FRESA")
chocolate = Base("DON CHOCOLATE",3200,15,9,False,"CHOCOLATE")
guanabana = Base("GUANABANAZO",4500,20,3,False,"GUANABANA")

"lista de ingredientes de complemento"
chispas_chocolate = Complemento("chispas",6500,15,2,False)
guanabanas = Complemento("Pulpa",12000,10,1,True)
fresas = Complemento("Fresas",18000,5,1,True)

"lista de ingredientes para cada producto"
list_ingredientes_copa_fresa = [fresa, fresas, fresas]
list_ingredientes_copa_chocolate = [chocolate, chispas_chocolate, chispas_chocolate]
list_ingredientes_guanabanas = [guanabanas, fresas, guanabanas]

"Creamos los 3 productos, cada uno con sus ingredientes"
copa_fresa = Copa("Fresass",8500,"Plasitco Gramde",list_ingredientes_copa_fresa)
copa_chocolate = Copa("Vaso Chocolate",17500,"Plasitco ",list_ingredientes_copa_chocolate)
malteada_guanabana = Malteada("Guabanazo",6500,75,list_ingredientes_guanabanas)

"Creamos la lista de productos"
lst_productos = [copa_fresa, copa_chocolate,malteada_guanabana]
print('1. Copa Fresa, retabilidad: {0}'.format(copa_fresa.calcular_rentabilidad()))
print('2. Copa Chocolate, retabilidad: {0}'.format(copa_chocolate.calcular_rentabilidad()))
print('3. Malteada Frutos, retabilidad: {0}'.format(malteada_guanabana.calcular_rentabilidad()))
print("\n")

print("### CONSTRUIR LA HELADERIA Y REALIZAR VENTAS")

"Creamos la Heladeria con los productos"
heladeria = Heladeria("Heladeria Fruppys", lst_productos)

print('La "{0}" tiene {1} productos.'.format(heladeria.get_nombre(),  lst_productos.__len__()))
print('El producto mas rentable es: {0}'.format(heladeria.producto_mas_rentable()))
print('Vender "Malteada de Chocolate":', heladeria.vender("Malteada de Chocolate"))
print("Ventas del dia:", heladeria.get_venta_del_dia())
print('Vender "Malteada de Coco":', heladeria.vender("Malteada de Coco"))
print("Ventas del dia:", heladeria.get_venta_del_dia())
print('Vender "Malteada Frutos Rojos":', heladeria.vender("Malteada Frutos Rojos"))
print("Ventas del dia:", heladeria.get_venta_del_dia())
