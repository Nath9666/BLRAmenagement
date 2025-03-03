from flask import Flask, jsonify
import json

app = Flask(__name__)

# Chemin du fichier JSON
json_file_path = './reformatted_table_data.json'

# Charger les données JSON au démarrage de l'application
with open(json_file_path, 'r') as file:
    lego_colors = json.load(file)

@app.route('/allColors', methods=['GET'])
def get_lego_data():
    return jsonify(lego_colors)

if __name__ == "__main__":
    app.run()