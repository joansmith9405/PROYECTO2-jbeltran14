import os
from flask import Flask, render_template
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from controllers.index_controller import IndexController
from controllers.heladeria_controller import HeladeriaController
from controllers.productos_controller import ProductosController
from controllers.ingredientes_controller import IngredientesController
from controllers.productos_ingredientes_controller import ProductosIngredientesController
from models.heladeria import Heladeria

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}/{os.getenv("SCHEMA_DB")}'
db.init_app(app)
api = Api(app)


@app.route("/")
def main():
    return "BIENVENIDOS"

@app.route("/index")
def menu():
    heladeria = Heladeria("La Heladeria")
    items = heladeria.__lista_productos()
    return render_template("index.html", items=items)





api.add_resource(IndexController, '/index')
api.add_resource(HeladeriaController, '/heladeria')
