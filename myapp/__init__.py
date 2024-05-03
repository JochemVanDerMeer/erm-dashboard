import os

from flask import Flask 

from .extensions import db
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    #postgresql://erm_dashboard_user:0pR6KYRY1gFbfDAMj1wEKRI2o4eRG5BN@dpg-contl121hbls73fqsld0-a.frankfurt-postgres.render.com/erm_dashboard

    db.init_app(app)

    app.register_blueprint(main)

    return app