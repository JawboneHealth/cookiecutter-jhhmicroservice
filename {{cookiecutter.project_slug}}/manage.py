#!/usr/bin/env python
"""
flask_script app manager
"""
import flask_script
import {{ cookiecutter.app_name }}.app


def make_app_context():
    return {'app': {{ cookiecutter.app_name }}.app}


#
# Manage commands
#
# App manager
#
app = {{ cookiecutter.app_name }}.app.create_app()
manager = flask_script.Manager(app)

#
# App Shell
#
manager.add_command("shell", flask_script.Shell(make_context=make_app_context))


if __name__ == '__main__':
    manager.run()
