# FastAPI & GraphQL

This is an example for using GraphQL with SQLAlchemy and FastAPI.
Do not use this in production for multiple reasons
(graphqli is activated, dev/prod packages are not separated, ...).

## Install

```
pip install -r requirements.txt
```

## Run

```
uvicorn gql_alchemy.app:app [--reload]
```

## Testing

```
export TESTING=True
pytest
unset TESTING
```

## Migrations

```
# add a migration
alembic revision -m "Name of the revision"

# add a migration with autogeneration
alembic revision --autogenerate -m "Name of the revision"

# more options
alembic --help
```
