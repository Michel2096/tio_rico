from flask import Blueprint

blueprint_home = Blueprint('home', _name_)
@blueprint_home.route('/home')
def home():
    return {'msn' : 'hola desde home'}