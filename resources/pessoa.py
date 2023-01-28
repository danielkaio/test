
from flask_restful import Resource, reqparse


pessoas = [
   
   {
    "cpf_id": "itapevi",
    "nome": " itapevi",
    "endereco":"dddd"
    
},



]

class Pessoas(Resource):
    def get(self):
        return {'Pessoas':pessoas}

class Pessoa(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument("cpf")
    argumentos.add_argument('endereco')


    def find_pessoa(cpf_id):
        for pessoa in pessoas:
            if pessoa['cpf_id'] == cpf_id:
                return pessoa
        return {"message":"hotel nao encontrado"}
        
        return None
    
    def get(self,cpf_id):
        pessoa = Pessoa.find_pessoa(cpf_id)
        if pessoa:
            return pessoa
    
        
    


    


    def post(self,cpf_id):
       
        dados = Pessoa.argumentos.parse_args()

        nova_pessoa = {  'cpf_id':cpf_id,**dados}
           
        pessoas.append(nova_pessoa)
        return nova_pessoa,200
        

  
    

    def put(self,cpf_id):
        dados = Pessoa.argumentos.parse_args()
        nova_pessoa = {  'cpf_id':cpf_id,**dados}
        pessoa = Pessoa.find_pessoa(cpf_id)
        if Pessoa  != "":
            pessoa.update(nova_pessoa)
            return nova_pessoa,200
        
          


            

  

    def delete(self,cpf_id):
        global pessoas
        pessoas  = [pessoa for pessoa in pessoas if pessoa ['cpf_id']!= cpf_id]
        return {'message':"pessoa excluida"}
