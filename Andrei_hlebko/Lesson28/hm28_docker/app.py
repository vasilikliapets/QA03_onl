from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return 'Hello World! My name is Andry Hlebko!'


api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
