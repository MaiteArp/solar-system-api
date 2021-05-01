from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path

db = SQLAlchemy()

migrate = Migrate()



def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
    
    if path.isfile("connection-string"):
        with open('connection-string', mode='r') as huzzah:
            what_i_read = huzzah.read()
            stripped = what_i_read.strip()
            connection_string = stripped
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string


    db.init_app(app)
    migrate.init_app(app, db)
    from .routes import planet_bp
    app.register_blueprint(planet_bp)

    from app.model.planet import Planet 
    

    return app
