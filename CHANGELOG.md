# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) 
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.2] - 2018-01-27
### Added
- Local alembic.ini file to run upgrades in the local env
- ALEMBIC_CONF config
- Added dc_port to cookiecutter JSON so we can specify the direct URL to the local service

### Changed
- Use `jhhalchemy.migrate` for alembic upgrades
- Update Dockerfile to reflect new infrastructure
- Bump Python to 2.7.15-slim
- Update `requirements.txt` to latest versions
- Update config.py to reflect new dependencies
- Renamed app directory to a user-specified app name that differs from the project directory

### Fixed
- Changed `USER_DB` to `DB_NAME` in configs

## [1.1] - 2018-01-09
### Added
- Options to use Alembic and SQLAlchemy
- Default logging level
- Post-generation hook script
- JWT package
- wait-for-it.sh in the Dockerfile
- Unit tests in the Jenkinsfile
