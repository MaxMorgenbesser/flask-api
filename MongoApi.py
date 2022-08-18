import flask
from flask import Flask
from flask import jsonify,request
import bson.json_util as json_util
from flask_cors import CORS

#connect to Mongo
import pymongo
from pymongo import MongoClient
import Secrets


app = flask.Flask(__name__)
cors=CORS(app)
app.config["DEBUG"] = True

secrets=Secrets.uri

def dbConnect(str):
    client = MongoClient(secrets)
    collection=client[str]
    return collection



dbCollection = dbConnect('Facebook-part-two')

@app.route('/get/collections', methods=['GET'])
def getAll():
    db = dbConnect('Facebook-part-two')
    dbcollections = db.list_collection_names()
    for collection in dbcollections:
        return collection

@app.route('/', methods=['GET'])
def Home():
    return '<h1>Home</h1>'



@app.route('/get', methods=['GET'])
def getAllMessages():
    results = []
    db = dbConnect('Facebook-part-two')
    collection=db['messages']
    all = collection.find({})
    for document in all:
        results.append(document)
    # print(results)
    #with app.app_context():
    return json_util.dumps(results)


# getAllMessges()


if __name__ == '__main__':
    with app.app_context():
        app.run()