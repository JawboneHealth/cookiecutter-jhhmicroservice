"""
The {{ cookiecutter.project_name }} microservice.

This module is responsible for Flask app, blueprint, and api initialization
"""
import flask
import httplib
import logging
import {{ cookiecutter.project_slug }}.api.v0_1
import {{ cookiecutter.project_slug }}.config
import {{ cookiecutter.project_slug }}.extensions
{% if cookiecutter.use_alembic == 'True' %}
import alembic.config
import alembic.command
import sqlalchemy_utils
{% endif %}


def create_app(config={{ cookiecutter.project_slug }}.config.Config):
    """
    Application factory

    :param config: app configuration module
    :return: Flask app object
    """
    #
    # Set the logging level according to the env
    #
    logging.getLogger().setLevel(config.LOG_LEVEL)

    {% if cookiecutter.use_alembic == 'True' %}
    if config.AUTO_UPGRADE:
        #
        # Run schema upgrades before bringing up the server.
        #
        if not sqlalchemy_utils.database_exists(config.SQLALCHEMY_DATABASE_URI):
            logging.info('Creating {}'.format(config.USER_DB))
            sqlalchemy_utils.create_database(config.SQLALCHEMY_DATABASE_URI)
        alembic_config = alembic.config.Config(
            'alembic/alembic.ini',
            attributes={'configure_logger': False})
        logging.info('Migrating DB to head')
        alembic.command.upgrade(alembic_config, 'head')
    {% endif %}

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
    {% if cookiecutter.use_sqlalchemy == 'True' %}
    {{cookiecutter.project_slug}}.extensions.db.init_app(app)
    {% endif %}
    {{cookiecutter.project_slug}}.extensions.ma.init_app(app)
    {{cookiecutter.project_slug}}.extensions.jwt.init_app(app)


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
