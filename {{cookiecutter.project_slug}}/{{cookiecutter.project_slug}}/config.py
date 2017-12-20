"""
Configuration items for server startup.
"""
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


#
# Set up config based on environment
#
ENV = os.environ.get('ENV')
config_class = '{}{}'.format(ENV.title(), 'Config') if ENV is not None else 'BaseConfig'
Config = globals()[config_class]
