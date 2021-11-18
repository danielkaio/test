
from flask_restful import Resource


hoteis = [
    {
        "hotel_id":"alpha",
        "nome": "alpha_hotel",
        "estrelas": 4.3,
        "diaria":4.500,
        "cidade":"rio de janeiro"
    },


     {
        "hotel_id":"alpha",
        "nome": "alpha_hotel",
        "estrelas": 4.3,
        "diaria":4.500,
         "cidade":"santos"
    },

     {
        "hotel_id":"alpha",
        "nome": "alpha_hotel",
        "estrelas": 4.3,
        "diaria":4.500,
        "cidade":"barueri"
    }
]

class Hoteis(Resource):
    def get(self):
        return {'Hoteis':hoteis}
