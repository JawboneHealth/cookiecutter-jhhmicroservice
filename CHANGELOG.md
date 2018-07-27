# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) 
and this project adheres to [Semantic Versioning](http://semver.org/).

## [1.2] - Unreleased
### Added
- Local alembic.ini file to run upgrades in the local env
- ALEMBIC_CONF config

### Changed
- Use `jhhalchemy.migrate` for alembic upgrades
- Update Dockerfile to reflect new infrastructure
- Bump Python to 2.7.15

## [1.1] - 2018-01-09
### Added
- Options to use Alembic and SQLAlchemy
- Default logging level
- Post-generation hook script
- JWT package
- wait-for-it.sh in the Dockerfile
- Unit tests in the Jenkinsfile
