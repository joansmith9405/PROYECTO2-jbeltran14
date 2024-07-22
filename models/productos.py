from db import db
from models.productos_ingredientes import ProductosIngredientes
import models.funciones as funciones


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    precio = db.Column(db.Float(), nullable=False)
    vaso = db.Column(db.String(), nullable=True)
    volumen = db.Column(db.Integer(), nullable=True)

    ingredientes = db.relationship('ProductosIngredientes', backref="ingredientes", lazy=True)

    def __init__(self, nombre: str, precio: float, vaso: str,  volumen: int, ingredientes: list):
        self.nombre = nombre
        self.precio = precio
        self.vaso = vaso
        self.volumen = volumen
        self.lista_ingredientes = ingredientes

    def calcular_calorias(self) -> float:
        lista_calorias = []
        for ingrediente in self.lista_ingredientes:
            lista_calorias.append(ingrediente.num_calorias)
        if self.vaso is None:
            return funciones.conteo_calorias(lista_calorias) + 200
        else:
            return funciones.conteo_calorias(lista_calorias)

    def calcular_costo(self) -> float:
        if self.vaso is None:
            return funciones.calcular_costo(self.lista_ingredientes) + 500
        else:
            return funciones.calcular_costo(self.lista_ingredientes)

    def calcular_rentabilidad(self):
        return funciones.calcular_rentabilidad(self.precio, self.lista_ingredientes)