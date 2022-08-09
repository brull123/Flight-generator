from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


class Hello(Resource):
    def get(self, dep, arr, plane, min_dist, max_dist):
        message = {"departure": dep,
                   "arrival": arr,
                   "airplane": plane,
                   "airline": "Aegean",
                   "pax": 138,
                   "dist":400
                   }
        return message


api.add_resource(
    Hello, "/api/<string:dep>/<string:arr>/<string:plane>/<string:min_dist>/<string:max_dist>")

if __name__ == "__main__":
    app.run(debug=True)
