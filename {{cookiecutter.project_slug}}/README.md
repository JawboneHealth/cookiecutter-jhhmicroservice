# {{ cookiecutter.project_name }}
{{ cookiecutter.project_name }} is a Flask microservice intended to run on the JHH platform.

## Install
Clone this repo:
```bash
$ git clone ssh://git@bitbucket.aliph.com:7999/jhh/{{ cookiecutter.project_slug }}.git
```

Set python version, create virtualenv, activate virtualenv, and install requirements:
```bash
$ pyenv local 2.7.15
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
### docker-compose
You can run this service as part of the API gateway's `docker-compose` network:
1. Create an entry for this service in the gateway's `docker-compose.yml` file.
1. Run `docker-compose up`

If you want to mount local code into the image running on that network:
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
schema migrations. When running alembic commands, the alembic.ini file is in a non-standard location in the alembic 
directory, so you must specify it at the command line:
```bash
$ alembic -c alembic/alembic.ini revision --autogenerate -m 'my new stuffs'
```
{% endif %}
{% endif %}

## Tests
There are some simple unit and integration tests written to run under pytest. After starting the service, run:
```bash
$ pytest
```