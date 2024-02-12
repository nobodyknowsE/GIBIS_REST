from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path
import glob
import os
import json

app = Flask(__name__)
CORS(app)

# Get modules
modules = {}

# Get Study course names from file names
ressourcesPath = r'rest\ressources\*long.json'
filePaths = glob.glob(ressourcesPath)
studyNames = []

for file in filePaths:
    with open(file, 'r') as json_datei:
        daten = json.load(json_datei)
    moduleName = os.path.basename(file).split("-module")[0]
    modules.update({moduleName : daten})
    studyNames.append(moduleName)

with open('test.json', 'w') as file:
    json.dump(modules, file, indent=2)

names = {'Studiengänge': studyNames}

#module als eine große json mit kürzel als zugriffspunkt
#von frontend kommt anfrage GET zugriffspunkt mit kürzel
#PUT kann dann auch über diesen Zugriffspunkt erfolgen


#GET
@app.get("/modules")
def get_modules():
    print(names)
    return jsonify(names)

#GET
@app.get("/course")
def get_course():
    course = request.args.get('id')
    return jsonify(modules[course])

if __name__ == "__main__":
    app.run(debug=True)