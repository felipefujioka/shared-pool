import flask
from main import app
from db.util import session
from auth.models.user import User

@app.route('/users', methods=['GET'])
def list_users():
    users = session.query(User).all()

    return str(dict(zip(users.keys(), users)))


@app.route('/users', methods=['POST'])
def create_user():
    body = flask.request.get_json()
    new_user = User(
        name=body.get('name'),
        email=body.get('email')
    )

    session.add(new_user)
    session.commit()

    return 'OK'
