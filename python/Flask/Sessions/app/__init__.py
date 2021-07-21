import os

from flask import Flask
from . import db, auth


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True,)
    app.config.from_mapping(
        SECRET_KEY=b'\xbfd2\x15\x90\x85\tQ\xff\x84\xe9[\xaa\xe8\xf0\xa6',
        DATABASE = os.path.join(app.instance_path, 'app.sqlite'),
    )
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Initialising database
    db.init_app(app)

    #Registering auth blueprint
    app.register_blueprint(auth.bp)

    # a simple page
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app
