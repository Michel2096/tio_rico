from flask import Flask
from controllers.HomeController import blueprint_home
from extension import db, migrate
from config import SQLALCHEMY_DATABASE_URI
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(blueprint_home)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5001)
