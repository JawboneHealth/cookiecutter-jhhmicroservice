"""
The {{ cookiecutter.project_name }} microservice.

This module is responsible for Flask app, blueprint, and api initialization
"""
import flask
import httplib
import logging
import {{ cookiecutter.app_name }}.api.v0_1
import {{ cookiecutter.app_name }}.config
import {{ cookiecutter.app_name }}.extensions
{% if cookiecutter.use_alembic == 'True' %}
import jhhalchemy.migrate
{% endif %}


def create_app(config={{ cookiecutter.app_name }}.config.Config):
    """
    Application factory

    :param config: app configuration module
    :return: Flask app object
    """

    #
    # Set the logging level according to the env
    #
    logging.getLogger().setLevel(config.LOG_LEVEL)

    app = flask.Flask(__name__)
    app.config.from_object(config)
    app.url_map.strict_slashes = False

    {% if cookiecutter.use_alembic == 'True' %}
    #
    # Run any new upgrades
    #
    if app.config.get('AUTO_UPGRADE'):
        jhhalchemy.migrate.upgrade(app.config.get('DB_NAME'),
                                   app.config.get('SQLALCHEMY_DATABASE_URI'),
                                   app.config.get('ALEMBIC_CONF'))
    {% endif %}

    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """
    Initialize Flask extensions.

    :param app: Flask app object
    """
    {% if cookiecutter.use_sqlalchemy == 'True' %}
    {{cookiecutter.app_name}}.extensions.db.init_app(app)
    {% endif %}
    {{cookiecutter.app_name}}.extensions.ma.init_app(app)
    {{cookiecutter.app_name}}.extensions.jwt.init_app(app)


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
        {% if cookiecutter.use_sqlalchemy == 'True' %}
        """
        Verify the DB is there.

        :return: 200 if all good, otherwise it raises an exception which returns 500
        """
        {{cookiecutter.app_name}}.extensions.db.session.query('1').from_statement('SELECT 1').all()
        {% endif %}
        return '', httplib.OK

    app.register_blueprint({{ cookiecutter.app_name }}.api.v0_1.get_blueprint())
