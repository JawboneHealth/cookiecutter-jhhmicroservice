#
# Dockerfile to create user service image
#
FROM python:2.7.13

#
# Environment Configuration
#
ENV PYTHONPATH /usr/src/app
ENV GU_WORKER_COUNT=2

#
# Grab wait-for-it
#
ADD https://raw.githubusercontent.com/Jawbone/wait-for-it/master/wait-for-it.sh /
RUN chmod +x /wait-for-it.sh

#
# App code dir
#
RUN mkdir -p /usr/src/app/{{ cookiecutter.project_slug}}
WORKDIR /usr/src/app

#
# Copy code into the container
#
COPY requirements.txt /usr/src/app/
COPY manage.py /usr/src/app/
COPY {{ cookiecutter.app_name }} /usr/src/app/{{ cookiecutter.project_slug }}/
{% if cookiecutter.use_alembic == 'True' %}
COPY alembic /usr/src/app/alembic/
{% endif %}

#
# Install dependencies
#
RUN pip install --index-url=https://pypi.jbnw.net/simple --extra-index-url=https://pypi.python.org/pypi --no-cache-dir -r requirements.txt

#
# Start the server.
#
CMD gunicorn -w ${GU_WORKER_COUNT} -b 0.0.0.0:5000 manage:app
