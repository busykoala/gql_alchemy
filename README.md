# FastAPI & GraphQL

## Install

```
pip install -r requirements.txt
```

## Run

```
uvicorn gql_alchemy.app:app [--reload]
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

## Testing

```
export TESTING=True
pytest
unset TESTING
```
