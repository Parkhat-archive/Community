from flask import Flask
import os
import dotenv
from config import DevelopmentConfig, TestingConfig, Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

from community_app.routers.questions import questions_bp
from community_app.routers.responses import response_bp


dotenv.load_dotenv()

app = Flask(__name__)
app.register_blueprint(questions_bp)
app.register_blueprint(response_bp)

config_name = os.getenv('FLASK_ENV')

config_set_up = {
    'production': Config,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}.get(config_name)

def create_app():

    app = Flask(__name__)
    app.config.from_object(config_set_up)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(questions_bp)
    app.register_blueprint(response_bp)

    return app
