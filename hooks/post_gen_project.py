"""
This runs automatically after creating a new microservice.
"""
import os
import shutil

#
# Clean up alembic if we're not using it
#
if not '{{ cookiecutter.use_alembic }}' == 'y':
    shutil.rmtree('alembic')
else:
    os.remove('alembic/versions/rm_this')

#
# Clean up models if we're not using them
#
if not '{{ cookiecutter.use_sqlalchemy }}' == 'y':
    shutil.rmtree('{{ cookiecutter.project_slug }}/models')
    shutil.rmtree('tests/unit/models')

#
# Remove cloudbuild yaml if we're not using it
#
if not '{{ cookiecutter.use_cloudbuild }}' == 'y':
    os.remove(os.path.join(os.getcwd(), 'cloudbuild.yaml'))

