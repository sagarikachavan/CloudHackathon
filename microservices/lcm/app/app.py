from flask import Flask
from flask_restful import Resource, Api
import math

app = Flask(__name__)
api = Api(app)

class LCM(Resource):
    def gcd(self,x,y):  
        # if(y==0):
        #     return x
        return math.gcd(x,y)
    def get(self,x,y,a,b):
        if a==1: x=-x
        if b==1: y=-y
        x=int(x)
        y=int(y)
        x1=max(x,y)
        x2=min(x,y)
        res=self.gcd(x1,x2)
        return (x*y)/res


api.add_resource(LCM,'/<float:x>/<float:y>/<int:a>/<int:b>')

if __name__ =='__main__':
    app.run(debug=True,port=5061,host="0.0.0.0")