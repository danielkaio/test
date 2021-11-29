
from flask_restful import Resource, reqparse


hoteis = [
   
   {
    "hotel_id": "itapevi",
    "nome": " itapevi",
    "diaria": "5.9",
    "estrelas": "2.5",
    "cidade": "sampa"
},

{
    "hotel_id": "santos",
    "nome": " santos",
    "diaria": "5.9",
    "estrelas": "2.5",
    "cidade": "sampa"
},


{
    "hotel_id": "bahia",
    "nome": " bahia",
    "diaria": "5.9",
    "estrelas": "2.5",
    "cidade": "sampa"
}

]

class Hoteis(Resource):
    def get(self):
        return {'Hoteis':hoteis}

class Hotel(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('diaria')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {"message":"hotel nao encontrado"}
        
        return None
    
    def get(self,hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
    
        
    


    


    def post(self,hotel_id):
       
        dados = Hotel.argumentos.parse_args()

        novo_hotel = {  'hotel_id':hotel_id,**dados}
           
        hoteis.append(novo_hotel)
        return novo_hotel,200
        

  

    




    def put(self,hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel = {  'hotel_id':hotel_id,**dados}
        hotel = Hotel.find_hotel(hotel_id)
        if hotel  != "":
            hotel.update(novo_hotel)
            return novo_hotel,200
        
          


            

  

    def delete(self,hotel_id):
        global hoteis
        hoteis  = [hotel for hotel in hoteis if hotel ['hotel_id']!= hotel_id]
        return {'message':"hotel excluido"}
