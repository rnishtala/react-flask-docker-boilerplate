from flask import Flask, redirect, url_for, jsonify, make_response
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
import json
import logging

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

mongoClient = MongoClient(
    'mongodb+srv://<>')
db = mongoClient.get_database('names_db')
names_col = db.get_collection('names_col')


@app.route('/addname/<name>/')
def addname(name):
    app.logger.info("====================")
    app.logger.info(name)
    names_col.insert_one({"name": name.lower()})
    return redirect(url_for('getnames'))


@app.route('/removename/<name>/')
def removename(name):
    app.logger.info("=======Removing name======")
    app.logger.info(name)
    names_col.remove({'name': name.lower()})
    return redirect(url_for('getnames'))


@app.route('/getnames/')
def getnames():
    app.logger.info("inside get names")
    names_json = []
    if names_col.find({}):
        for name in names_col.find({}).sort("name"):
            names_json.append({"name": name['name'], "id": str(name['_id'])})
    # app.logger.info(json.dumps(names_json))
    # response = make_response(jsonify(names_json))
    # app.logger.info(json.dumps(response.json()))
    # response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    app.logger.info(json.dumps(names_json))
    return json.dumps(names_json)


if __name__ == "__main__":
    app.run(debug=True)
