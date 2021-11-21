
from flask_restful import Resource, reqparse


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
        return {"message":"hotel nao existe"}
           


    def post(self,hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('diaria')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('cidade')

        dados = argumentos.parse_args()

        novo_hotel = {
             'hotel_id':hotel_id,
            'nome':dados['nome'],
            'diaria':dados[ 'diaria'],
            'estrelas':dados['estrelas'],
            'cidade':dados['cidade']


        }
        hoteis.append(novo_hotel)
        return novo_hotel,200
        

  

    




    def put(self):
        pass

    def delete(self):
        pass
