from bson import json_util,ObjectId
from flask import Flask,request,jsonify
from pymongo import MongoClient
from apisw import *


app = Flask(__name__)
app.testing = True

client = MongoClient("mongodb://gabrielbur:ab12cd34@ds233531.mlab.com:33531/starwarsdb")
db = client.starwarsdb


##GetAll
@app.route('/planets',methods=['GET'])
def get_all_planets():
    output=[] 
    planets = db.planets
    
    for p in planets.find():
        output.append({'ID':json_util.dumps(p['_id']),'Nome':p['Nome'],'Clima':p['Clima'],'Terreno':p['Terreno'],'QtdFilmes':p['QtdFilmes']})      
    
    return jsonify({'result':output})



##GetById
@app.route('/planets/<string:Id>',methods=['GET'])
def get_planets_by_id(Id):
    planets = db.planets
    p = planets.find_one({'_id':ObjectId(Id)})

    if p:
        output = {'ID':json_util.dumps(p['_id']),'Nome':p['Nome'],'Clima':p['Clima'],'Terrano':p['Terreno']}
    else:
        output = "Sem resultados"
        
    return jsonify({'result':output})



##GetByName
@app.route('/planets/name/<string:Nome>',methods=['GET'])
def get_planets_by_name(Nome):
    planets = db.planets
    
    p = planets.find_one({'Nome':Nome})
    
    if p:
        output = {'ID':json_util.dumps(p['_id']),'Nome':p['Nome'],'Clima':p['Clima'],'Terrano':p['Terreno']}
    else:
        output = "Sem resultados"
        
    return jsonify({'result':output})




##Create
@app.route('/planets',methods=['POST'])
def create_planet():  
    planets = db.planets   
    nome = request.json['Nome']
    clima = request.json['Clima']
    terreno = request.json['Terreno']
    
    aparicoes = getCountPlanets(nome)

    planet_id = planets.insert({'Nome':nome,'Clima':clima,'Terreno':terreno,'QtdFilmes':aparicoes})
    new_planet = planets.find_one({'_id':planet_id})
 
    output = {'ID':json_util.dumps(new_planet['_id']),'Nome':new_planet['Nome'],'Clima':new_planet['Clima'],'Terreno':new_planet['Terreno']}

    return jsonify({'result':output})



##Delete
@app.route('/planets/<string:Id>',methods=['DELETE'])
def delete_planet(Id):
    planets = db.planets
    
    try:
        output = planets.delete_one({'_id':ObjectId(Id)})
        if output.deleted_count==1:
            output="Registro Deletado"
        else:
            output="Registro não encontrado"
        return jsonify({'result':output})
    except:
        output = "Sem resultados"
        return jsonify({'result':output})



