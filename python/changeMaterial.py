import json

# Chemin du fichier JSON
file_path = '../assets/Material/material_brinklinks.json'

# Fonction pour convertir une couleur hexadécimale en RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Fonction pour déterminer si une couleur est transparente
def is_transparent(color_type):
    return color_type.lower() == 'transparent'

# Fonction pour ajouter les nouvelles valeurs et supprimer les anciennes
def reformat_data(data):
    reformatted_data = {}
    for item in data:
        for key, value in item.items():
            hex_color = value['bgColor']
            reformatted_data[key] = {
                'name': value['name'],
                'rgb': hex_to_rgb(hex_color),
                'hex': "#"+hex_color,
                'metallic': 0.2 if 'Solid' in value['type'] else 0.8,
                'roughness': 0.5 if 'Solid' in value['type'] else 0.3,
                'transparent': is_transparent(value['type'])
            }
    return reformatted_data

# Lecture du fichier JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# Reformater les données
reformatted_data = reformat_data(data)

# Écriture des données reformattées dans un nouveau fichier JSON
with open('../assets/Material/material_reformated.json', 'w') as file:
    json.dump(reformatted_data, file, indent=2)

print("Données reformattées et enregistrées avec succès.")