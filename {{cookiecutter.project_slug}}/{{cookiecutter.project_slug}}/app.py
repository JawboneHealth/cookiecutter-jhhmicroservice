"""
The {{ cookiecutter.project_name }} microservice.

This module is responsible for Flask app, blueprint, and api initialization
"""
import flask
import httplib
import {{ cookiecutter.project_slug }}.api.v0_1
import {{ cookiecutter.project_slug }}.config
import {{ cookiecutter.project_slug }}.extensions


def create_app(config={{ cookiecutter.project_slug }}.config.Config):
    """
    Application factory

    :param config: app configuration module
    :return: Flask app object
    """
    app = flask.Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """
    Initialize Flask extensions.

    :param app: Flask app object
    """
    {{cookiecutter.project_slug}}.extensions.ma.init_app(app)


def register_blueprints(app):
    """
    Create simple routes and then register api blueprints.

    :param app: Flask app object
    """
    @app.route('/')
    def hello():
        return '<html><body>{{ cookiecutter.project_name }} - Hello World</body></html>'

    @app.route('/healthz')
    def healthz():
        return '', httplib.OK

    app.register_blueprint({{ cookiecutter.project_slug }}.api.v0_1.get_blueprint())
