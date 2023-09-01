from flask import Flask
from flask_restful import Resource, Api
import math
app = Flask(__name__)
api = Api(app)

class GCD(Resource):
    def get(self,x,y,a,b):
        x=int(x)
        y=int(y)
        if a==1: x=-x
        if b==1: y=-y
        res=math.gcd(x,y)
        return res


api.add_resource(GCD,'/<float:x>/<float:y>/<int:a>/<int:b>')

if __name__ =='__main__':
    app.run(debug=True,port=5060,host="0.0.0.0")