
from flask_restful import Resource


hoteis = [
    {
        "hotel_id":"bravo",
        "nome": "alpha_hotel",
        "estrelas": 4.3,
        "diaria":4.500,
        "cidade":"rio de janeiro"
    },


     {
        "hotel_id":"tela",
        "nome": "alpha_hotel",
        "estrelas": 4.3,
        "diaria":4.500,
         "cidade":"santos"
    },

     {
        "hotel_id":"aranha",
        "nome": "alpha_hotel",
        "estrelas": 4.3,
        "diaria":4.500,
        "cidade":"barueri"
    }
]

class Hoteis(Resource):
    def get(self):
        return {'Hoteis':hoteis}

class Hotel(Resource):
    def get(self,hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
           


        
            
           
       
            

    def post(self):
        pass


    def put(self):
        pass

    def delete(self):
        pass
