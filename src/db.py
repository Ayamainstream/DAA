from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
import jwt 
import datetime
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/databasename'
db = SQLAlchemy(app)

class Users(db.Model):

    tablename = 'users'

    id = db.Column('id', db.Integer, primary_key=True)

    login = db.Column('login', db.String(50))

    password = db.Column('password', db.String(50))

    token = db.Column('token', db.String(50))

    def init(self,id,login, password, token):
        self.id = id
        self.login = login
        self.password = password
        self.token = token

app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return '<h1>There is no token<h1>'
        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return '<h1>Hello, Could not verify the token </h1>'

        return f(*args, **kwargs)

    return decorated


@app.route('/protected')
@token_required
def protected():
    return '<h1>Hello, token which is provided is correct </h1>'

@app.route('/login')
def login():
    auth = request.authorization
    login = ""
    if auth:
        login = auth.username
        users = Users.query.filter_by(login=auth.username).first()
        if users:
            if users.password == auth.password:
                token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=30)}, app.config['SECRET_KEY'])
                update_this = Users.query.filter_by(id=users.id).first()
                update_this.token = token.decode('UTF-8')
                db.session.commit()
            return jsonify({'token' : token.decode('UTF-8')})
    return make_response(f'<h1>Could not found a user with login: {login}</h1>', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


if __name__ == '__main__':
    app.run(debug=True)