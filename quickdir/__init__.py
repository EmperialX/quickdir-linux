from flask import Flask

def create_app():
    app = Flask(__name__)

    from .quickdir import quickdir as quickdir_blueprint
    app.register_blueprint(quickdir_blueprint)

    return app
