"""
Configuration items for server startup.
"""
import logging
import os


class BaseConfig(object):
    """
    Base configuration.
    """
    V0_1_PATH = '/{{ cookiecutter.project_slug }}/api/v0.1'

    #
    # Debug toolbar
    #
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    #
    # Flask-Restplus
    #
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False

    #
    # JWT Configuration
    #
    JWT_SECRET = 'datalogy'  # SECURITY VULNERABILITY!

    {% if cookiecutter.use_sqlalchemy == 'True' %}
    #
    # SQLAlchemy path
    #
    DB_NAME = '{{ cookiecutter.database }}'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@mysql/{}'.format(DB_NAME)
    #
    # Mysql Pool
    #
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_RECYCLE = 500
    {% endif %}

    #
    # Alembic
    #
    { % if cookiecutter.use_alembic == 'True' %}
    AUTO_UPGRADE = False
    { % endif %}

    #
    # Logging
    #
    LOG_LEVEL = logging.NOTSET

    ALEMBIC_CONF = 'alembic/alembic.ini'


class DevConfig(BaseConfig):
    """
    Development configuration.
    """
    ENV = 'dev'
    DEBUG = True

    #
    # Flask debug toolbar
    #
    DEBUG_TB_ENABLED = True

    {% if cookiecutter.use_alembic == 'True' %}
    #
    # Alembic auto-bootstrapping
    #
    AUTO_UPGRADE = True
    {% endif %}


class StageConfig(BaseConfig):
    """
    Staging configuration.
    """
    ENV = 'stage'



class ProdConfig(BaseConfig):
    """
    Production Configuration
    """
    ENV = 'prod'  # TODO check against pod node label
    JWT_SECRET = os.getenv('JWT_SECRET')
    LOG_LEVEL = logging.WARN


#
# Set up config based on environment
#
ENV = os.environ.get('ENV')
config_class = '{}{}'.format(ENV.title(), 'Config') if ENV is not None else 'BaseConfig'
Config = globals()[config_class]
