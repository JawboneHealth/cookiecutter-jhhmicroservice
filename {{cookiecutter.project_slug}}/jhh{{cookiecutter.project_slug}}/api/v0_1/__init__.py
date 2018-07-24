"""
Initializes the blueprint and namespaces.
"""
import flask
import flask_restplus
import jhh{{ cookiecutter.project_slug }}.config


def get_blueprint():
    """
    THIS SHOULD ONLY GET CALLED DURING SERVER STARTUP.
    It creates the blueprint, api, and namespaces for v0.1 of the user APIs.

    The call stack for this is
    app.create_app -> app.register_blueprints -> v0_1.get_blueprint

    Calling this outside of server startup will at best do nothing but could
    lead to incorrect routing of the APIs.

    :return: the blueprint
    """
    v0_1_bp = flask.Blueprint(
        jhh{{cookiecutter.project_slug}}.config.Config.V0_1_PATH,
        __name__,
        url_prefix=jhh{{ cookiecutter.project_slug }}.config.Config.V0_1_PATH)
    v0_1_api = flask_restplus.Api(
        v0_1_bp,
        title='{{ cookiecutter.project_name }} API v0.1',
        version='0.1',
        description='{{ cookiecutter.project_name }} API v0.1'
    )

    #
    # Add namespaces to the API
    #

    return v0_1_bp
