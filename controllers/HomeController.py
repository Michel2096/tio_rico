from flask import Blueprint

blueprint_home = Blueprint("home", __name__)

@blueprint_home.route("/")
def home():
    return {"message": "API Flask funcionando correctamente"}, 200
