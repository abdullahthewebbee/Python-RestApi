# Basic REST API in Python

Example of how to create a basic REST API in Python.

The key components of an API are:

- get inputs
- validate inputs
- logging
- database queries
- check database response (success vs. failure)
- http response
    - standardized messaging in response
    - error responses
    - success responses
- browsable API documentation


- Installation
- Configuration
- Live reload
- Task runner
- Code generation
- Debugging
- Testing

## Dependencies

- Flask: micro-framework for building APIs
- schematics: validation
- psycopg2: PostgreSQL
- cassandra-python: Cassandra


## Steps

- Install Oracle JDK
- Install PyCharm
- Install virtualenv/virtualenvwrapper

```bash
pip install Flask schematics six
```


```bash
mkdir -p ~/repos/basic-python-rest-api && cd $_
```

```bash
vi api.py
```

## Start/stop server

```bash
export API_CONFIG=/path/to/api_config.py

python server.py
```

## Files

`./server.py`

Startup script that calls `api/__init__.py`.

`api/__init__.py`

Create the flask app and import all routes.

`<some package name>/*.py`

All of the Python files that are used to create REST endpoints and the function
that each endpoint is mapped to.
