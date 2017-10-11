import flask
from jsonschema import validate, ValidationError
import simplejson
import errors
from functools import wraps


def validate_body(schema):
    def wrapper_func(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                flask.request.parsed_body = simplejson.loads(flask.request.data)
            except simplejson.scanner.JSONDecodeError:
                raise errors.ClientError('Body must be a valid json')

            try:
                validate(flask.request.parsed_body, schema)
            except ValidationError as e:
                raise errors.ClientError(str(e))

            return f(*args, **kwargs)
        return decorated_function
    return wrapper_func
