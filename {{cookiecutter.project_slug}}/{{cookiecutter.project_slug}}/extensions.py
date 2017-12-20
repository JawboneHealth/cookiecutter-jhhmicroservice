"""
Create and initialize Flask extensions.
"""
import flask_debugtoolbar
import flask_marshmallow


ma = flask_marshmallow.Marshmallow()
debug_toolbar = flask_debugtoolbar.DebugToolbarExtension()
