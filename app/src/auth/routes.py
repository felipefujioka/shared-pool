import flask
from main import app
from db.util import session
from auth.models.user import User
from auth.models.password_credential import PasswordCredential
import scrypt
import decorators.validate
import os
import errors


create_user_schema = {
    "type": "object",
    "required": [
        'name',
        'email',
        'password',
        'confirmation_password'
    ],
    "additional_properties": False,
    "properties": {
        "email": {
            "type": "string",
            "pattern": "^(([^<>()\[\]\\.,;:\s@""]+(\.[^<>()\[\]\\.,;:\s@""]+)*)|(\.+))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
        },
        "name": {
            "type": "string"
        },
        "password": {
            "type": "string",
            "minimum_length": 8
        },
        "confirmation_password": {
            "type": "string",
            "minimum_length": 8
        }
    }
}


def hash_password(password, maxtime=0.5, datalength=64):
    return scrypt.encrypt(os.urandom(datalength), password, maxtime=maxtime)


@app.route('/users', methods=['GET'])
def list_users():
    users = session.query(User).all()

    return str(dict(zip(users.keys(), users)))


@app.route('/users', methods=['POST'])
@decorators.validate.validate_body(create_user_schema)
def create_user():
    body = flask.request.parsed_body

    if body.get('password') != body.get('confirmation_password'):
        raise errors.UnprocessableEntityError('password and confirmation does not match')

    try:

        new_user = User(
            name=body.get('name'),
            email=body.get('email')
        )

        session.add(new_user)

        user = session.query(User).where(User.email == body.get('email')).get(1)

        new_password = PasswordCredential(
            user_id=user.id,
            password_hash=hash_password(body.get('password'))
        )
        session.add(new_password)
        session.commit()
    except Exception as e:
        session.rollback()
        raise errors.UnprocessableEntityError('DB error: {}'.format(e))


    return 'OK'
