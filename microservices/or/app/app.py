from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Or(Resource):
    def get(self,x,y):
        x,y = int(x),int(y)
        return x|y


api.add_resource(Or,'/<float:x>/<float:y>')

if __name__ =='__main__':
    app.run(debug=True,port=5063,host="0.0.0.0")