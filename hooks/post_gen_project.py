"""
This runs automatically after creating a new microservice.
"""
import os
import shutil

#
# Clean up alembic if we're not using it
#
if not {{ cookiecutter.use_alembic }}:
    shutil.rmtree('alembic')
else:
    os.remove('alembic/versions/rm_this')

#
# Clean up models if we're not using them
#
if not {{ cookiecutter.use_sqlalchemy }}:
    shutil.rmtree('{{ cookiecutter.project_slug }}/models')
    shutil.rmtree('tests/unit/models')
