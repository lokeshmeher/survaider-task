from flask import Flask, url_for, render_template, jsonify, request
from flask_pymongo import PyMongo
import json
from pprint import pprint

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'appdb_free'
app.config['MONGO_URI'] = 'mongodb://lokesh:pa$$w0rd123@ds145355.mlab.com:45355/appdb_free'

# Instantiate database connection
mongo = PyMongo(app)

@app.cli.command('initdb')
def init_db():
	"""Insert data from json file into database."""
	topics = mongo.db.topics	# Create a collection named `topics`.
	with open('challenge.json') as data_file:
		data = json.load(data_file)
		topics.insert(data)
	print('Initialized database.')


@app.route('/', methods=['GET'])
def home():
	"""Home page."""
	return render_template('home.html')


@app.route('/get_names', methods=['GET'])
def get_names():
	"""Returns the list of names of the users."""
	topics = mongo.db.topics
	names = set()
	for topic in topics.find():
		for person in topic['followers']:
			names.add(person['name'])
	return jsonify({'names': [name for name in names]})


@app.route('/get_topics', methods=['GET'])
def get_topics():
	name = request.args.get('name')
	topics = mongo.db.topics.find({'followers': {'name': name}})
	return jsonify({'topics': [doc.topic for doc in topics]})
