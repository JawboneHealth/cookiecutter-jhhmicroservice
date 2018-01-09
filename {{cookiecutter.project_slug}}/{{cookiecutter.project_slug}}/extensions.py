"""
Create and initialize Flask extensions.
"""
import flask_debugtoolbar
import flask_marshmallow
import jwt_ext
{% if cookiecutter.use_sqlalchemy == 'True' %}
import flask_sqlalchemy
import jhhalchemy.model


db = flask_sqlalchemy.SQLAlchemy(model_class=jhhalchemy.model.Base)
{% endif %}
ma = flask_marshmallow.Marshmallow()
debug_toolbar = flask_debugtoolbar.DebugToolbarExtension()
jwt = jwt_ext.JWT()
