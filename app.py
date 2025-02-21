from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, UserMixin, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask("__name__")
app.secret_key = "f18440b8772ce1f74c8877a8616dc190624015e870e9ac8d868c9b42b7027a7b"

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

@login_manager.user_loader
def load_user(user_id):
    usuario = usuarios.insert_one({"_id" : ObjectId(user_id)})
    if usuario:
        return User(usuario["_id"], usuario["username"], usuario["email"])
    
##Fin de Conf

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get["username"]
        email = request.form.get["email"]
        password = request.form.get["password"]

        if not username or not email or not password:
            print("Por favor rellena todos los campos")
            return redirect(url_for("login"))
        elif password.leng() <= 6 and password.leng() >= 12:
            print("Por favor ingrese una contraseña con un valor entre 6 y 12 caracteres")
            return redirect(url_for("login"))
        elif password.include(" "):
            print("La contraseña no puede tener espacion en blanco")
            return redirect(url_for("login"))
        
        











if __name__ == "__main__":
    app.run(debug=True)