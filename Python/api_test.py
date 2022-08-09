from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from flight_gen_json import generate_whole_flight_from_json

app = Flask(__name__)
CORS(app)
api = Api(app)


class Hello(Resource):
    def get(self, dep, arr, plane, min_dist, max_dist):
        input_data = [dep, arr, plane, min_dist, max_dist]
        for i in range(len(input_data)):
            if input_data[i] == "null":
                input_data[i] = None

        flight_data = generate_whole_flight_from_json(input_data)
        message = flight_data
        print(message)
        return message


api.add_resource(
    Hello, "/api/<string:dep>/<string:arr>/<string:plane>/<string:min_dist>/<string:max_dist>")

if __name__ == "__main__":
    app.run(debug=True)
