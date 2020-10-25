from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import identity, authenticate

app = Flask(__name__)
# app.secret_key = 'shubham'
api = Api(app)

# jwt = JWT(app, authenticate, identity)

class Student(Resource):
    # @jwt_required
    def get(self, name: str):
        return {'Student_name': name}


if __name__ == '__main__':
    api.add_resource(Student, '/Student/<string:name>')
    app.run(debug=True)
