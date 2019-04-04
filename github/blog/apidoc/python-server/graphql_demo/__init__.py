import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(*args, **kwargs):
    """
    Creating instance Flask application
    :param args: unnamed arguments.
    :param kwargs: key-valued arguments.
    :return: Flask app instance
    """
    # Support custom app_config for extensive purposes.

    from flask import Flask

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    return app


app = create_app()
db = SQLAlchemy(app)
from graphql_demo import router, model, schema
