from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Add(Resource):
    def get(self,x,y,a,b):
        if a==1: x=-x
        if b==1: y=-y
        return x+y


api.add_resource(Add,'/<float:x>/<float:y>/<int:a>/<int:b>')

if __name__ =='__main__':
    app.run(debug=True,port=5051,host="0.0.0.0")