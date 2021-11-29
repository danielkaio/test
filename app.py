from flask import Flask
from flask_restful import   Api
from resources.hotel import Hoteis, Hotel


app = Flask(__name__)

api = Api(app)


@app.route("/")
def index():
    return "lista de hotéis"
    



api.add_resource(Hoteis,"/hoteis")
api.add_resource(Hotel,"/hoteis/<string:hotel_id>")

if __name__ == "__main__":
    app.run(debug=True)