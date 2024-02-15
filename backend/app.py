from flask import Flask, request, jsonify
from flask_cors import CORS
import glob
import os
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

# BUILD UP DICT OF COURSES AND MODULES
modules = {} # dict of all courses and associated modules
studyNames = [] # list of '20inb', '20min',...
ressourcesPath = 'ressources/*long.json'
filePaths = glob.glob(ressourcesPath)

for file in filePaths:
    with open(file, 'r', encoding='utf-8') as json_datei:
        daten = json.load(json_datei)
    courseName = os.path.basename(file).split("-module")[0]
    studyNames.append(courseName)
    modules.update({courseName : daten})

courses = {'Studiengänge': studyNames}

# DEFINE END POINTS
@app.get("/courses")
def get_modules():
    return jsonify(courses)

@app.get("/course")
def get_course():
    course = request.args.get('id')
    return jsonify(modules[course])

@app.post("/login")
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == 'admin' and password == 'gibis':
        return jsonify({'message': 'Erfolgreich angemeldet!'}), 200
    else:
        return jsonify({'error': 'Falscher Benutzername oder Passwort!'}), 401

@app.post("/modules")
def add_module():
    if request.is_json:
        module = request.get_json()
        course = request.args.get('id')
        modules[course].insert(0, module)
        return module, 201
    return {"error": "Request must be JSON"}, 415

# RUN APP
if __name__ == "__main__":
    app.run(debug=True)