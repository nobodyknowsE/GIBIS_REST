from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

modules = [{
    "Modul": "Modellierung",
    "Modulnummer": "C114.2",
    "Art": "Pflichtmodul",
    "ECTS": 8,
    "SWS": "4/0/2/0",
    "Prüfungsleistung": ["PVB", "PVP", "PK"]
  },
  {
    "Modul": "Digitaltechnik I",
    "Modulnummer": "C752.1",
    "Art": "Pflichtmodul",
    "ECTS": 8,
    "SWS": "3/0/2/0",
    "Prüfungsleistung": ["PVB", "PK"]
  }
]

#GET
@app.get("/modules")
def get_modules():
    return jsonify(modules)

if __name__ == "__main__":
    app.run(debug=True)