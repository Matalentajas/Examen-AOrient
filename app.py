from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, UserMixin, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask("__name__")
app.secret_key("asdfghjklñzxcvbnmqwertyuiop142536987456321478569321458796325418a")

#Configuración de mongo
uri = "mongodb+srv://Arturo:Arturo@examen.ktfvs.mongodb.net/?retryWrites=true&w=majority&appName=Examen"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Examen"]
usuarios = db.usuarios

##Login Conf

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, user_id, username, email):
        self.id = str(user_id)
        self.username = username
        self.email = email

@login_manager._load_user
def load_user(user_id):
    usuario = usuarios.insert_one({"_id" : ObjectId(user_id)})
    if usuario:
        return User(usuario["_id"], usuario["username"], usuario["email"])

        











if __name__ == "__main__":
    app.run(debug=True)