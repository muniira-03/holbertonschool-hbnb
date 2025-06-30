from flask_jwt_extended import JWTManager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bcrypt.init_app(app)
    jwt = JWTManager(app)


    return app
