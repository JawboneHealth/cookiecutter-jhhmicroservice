#
# Dockerfile to create user service image
#
FROM python:2.7.15

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
RUN mkdir -p /usr/src/app/{{ cookiecutter.app_name}}
WORKDIR /usr/src/app

#
# Copy code into the container
#
COPY requirements.txt /usr/src/app/
RUN pip install \
    --trusted-host pypi.infra.jawbonr.com \
    --extra-index-url http://pypi.infra.jawbonr.com/simple/ \
    --no-cache-dir -r requirements.txt

COPY manage.py /usr/src/app/
COPY {{ cookiecutter.app_name }} /usr/src/app/{{ cookiecutter.app_name }}/
{% if cookiecutter.use_alembic == 'True' %}
COPY alembic /usr/src/app/alembic/
{% endif %}
COPY tests /usr/src/app/tests

#
# Start the server.
#
ENTRYPOINT ["gunicorn", "-w", "2", "--timeout", "120", "-b", "0.0.0.0:5000", "manage:app"]
