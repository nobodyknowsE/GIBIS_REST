from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path
import glob
import os

app = Flask(__name__)
CORS(app)

# Get modules
modules = {}

# Get Study course names from file names
ressourcesPath = r'rest\ressources'
filePaths = Path(ressourcesPath).glob('*.json')
fileNames = [os.path.basename(file) for file in filePaths]

for file in filePaths:
    with file.open('r') as f:
        content = f.read()


studyNames = [name.split("-modul")[0] for name in fileNames]
names = {'Studiengänge': studyNames}

#module als eine große json mit kürzel als zugriffspunkt
#von frontend kommt anfrage GET zugriffspunkt mit kürzel
#PUT kann dann auch über diesen Zugriffspunkt erfolgen


#GET
@app.get("/modules")
def get_modules():
    return jsonify(names)

if __name__ == "__main__":
    app.run(debug=True)