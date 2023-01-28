from flask import Flask
from flask_restful import   Api
from resources.pessoa import Pessoa, Pessoas


app = Flask(__name__)

api = Api(app)


@app.route("/")
def index():
    return "lista de hotéis"
    



api.add_resource(Pessoas,"/pessoas")
api.add_resource(Pessoa,"/pessoas/<string:cpf_id>")

if __name__ == "__main__":
    app.run(debug=True)