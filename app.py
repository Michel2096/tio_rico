from flask import Flask
from controllers.HomeController import blueprint_home

def create_app():
    app = Flask(_name_)
    app.register_blueprint(blueprint_home)
    @app.route('/')
    def home():
        return{'mensaje': 'hola mundo'},400
    
    return app

if _name_ == 'main':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5001)