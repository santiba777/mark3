import flask
from flask import jsonify
from flask import request
import creds
from sql import create_connection
from sql import execute_read_query

app = flask.Flask(__name__)
app.config["DEBUG"] = True


video_games = [
    {'id': 0,
     'name': 'Urbanchause',
     'genero': 'peleas',
     'consola': 'playstion'
     },
    {'id': 1,
     'name': 'jak and daxter',
     'genero': 'aventuras',
     'consola': 'xbox'
     },
    {'id': 2,
     'name': 'taken',
     'genero': 'peleas',
     'consola': 'nitendo'
     },
 ]

@app.route('/', methods=['GET'])
def home():
    return "<h1> WELLCOME TO THE NEW VIDEO GAMES </h1>"

@app.route ('/api/videogame/all', methods=['GET'])
def api_all():
    return jsonify(video_games)

@app.route('/api/videogame' , methods=['GET'])
def api_id():
    if 'id' in request.args:
      id = int(request.args['id'])
    else:
      return "Error: NO ID PROVIDED"
    results = []
    for videogame in video_games:
      if videogame ['id'] == id:
            results.append(videogame)
      return jsonify(results)


app.run()