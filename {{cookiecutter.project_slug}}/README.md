# {{ cookiecutter.project_name }}
{{ cookiecutter.project_name }} is a Flask microservice intended to run on the JHH platform.

## Install
Clone this repo:
```bash
$ git clone ssh://git@bitbucket.aliph.com:7999/jhh/{{ cookiecutter.project_slug }}.git
```

Set python version, create virtualenv, activate virtualenv, and install requirements:
```bash
$ pyenv local 2.7.13
$ virtualenv <VIRTUALENV_DIR>/{{ cookiecutter.project_slug }}
$ . <VIRTUALENV_DIR>/{{ cookiecutter.project_slug }}/bin/activate
$ pip install -r requirements.txt
```

## Build
Build a local image from the root directory of this project:
```bash
$ docker build -t {{ cookiecutter.project_slug }}:local .
```

## Run
### Local
You can run the Flask server locally:
```bash
$ export ENV=dev
$ ./manage.py runserver
```

### Docker
Once you build the Docker image, you can run it independently:
```bash
$ docker run -e "ENV=dev" -d -p 5000:5000 {{ cookiecutter.project_slug }}:local
```

### docker-compose
You can also run this service as part of the API gateway `docker-compose` network. If you want to mount local code into
the image running on that network:
```bash
$ cd <npgateway_DIR>
$ docker-compose -f docker-compose.yml -f ../{{ cookiecutter.project_slug }}/docker-compose.yml up
```

{% if (cookiecutter.use_sqlalchemy == 'True') or (cookiecutter.use_alembic == 'True') %}
## Database 
{% if cookiecutter.use_sqlalchemy == 'True' %}
### Flask-SQLAlchemy
{{ cookiecutter.project_name }} uses [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) to connect to the Maria Database.
To create models, refer to [this](http://flask-sqlalchemy.pocoo.org/2.3/models/) and to the [SQLAlchemy Declarative 
documentation](http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/).  
{% endif %}
{% if cookiecutter.use_alembic == 'True' %}
### Alembic
{{ cookiecutter.project_name }} uses [Alembic](http://alembic.zzzcomputing.com/en/latest/) to generate and run database 
schema migrations.
{% endif %}
{% endif %}

## Tests
There are some simple unit and integration tests written to run under pytest. After starting the service, run:
```bash
$ pytest
```