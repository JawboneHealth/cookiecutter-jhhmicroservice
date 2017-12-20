#!/usr/bin/env python
"""
flask_script app manager
"""
import flask_script
import {{ cookiecutter.project_slug }}.app


def make_app_context():
    return {'app': {{ cookiecutter.project_slug }}.app}


#
# Manage commands
#
# App manager
#
app = {{ cookiecutter.project_slug }}.app.create_app()
manager = flask_script.Manager(app)

#
# App Shell
#
manager.add_command("shell", flask_script.Shell(make_context=make_app_context))


if __name__ == '__main__':
    manager.run()
