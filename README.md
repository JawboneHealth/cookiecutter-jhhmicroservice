# cookiecutter-jhhmicroservice
Cookiecutter to create a Flask microservice to run on the JHH platform

## Create the microservice
First you must have cookiecutter installed:
```bash
$ pip install cookiecutter
```
In the directory, where you want your new microservice repo to live, run:
```bash
$ cookiecutter gh:JawboneHealth/cookiecutter-jhhmicroservice
```

## Template Variables
Variable | Description
---------|------------
project_name | Human readable name of your microservice
project_slug | Machine-friendly version of project_name (directories/code/etc. will use this)
use_sqlalchemy | True/False whether to include SQLAlchemy modules/code for MariaDB
database | Name of the primary database
use_alembic | True/False whether to include Alembic modules/code for MariaDB schema migrations

## Next Steps
Once you've created your new microservice, refer to its README for details on developing, running, and testing it.