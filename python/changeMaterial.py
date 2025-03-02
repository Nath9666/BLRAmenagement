"""
changeMaterial.py

Ce script lit un fichier JSON contenant des informations sur des matériaux,
reformate les données en ajoutant des valeurs supplémentaires, puis écrit les données 
reformattées dans un nouveau fichier JSON.
"""

import json

# Chemin du fichier JSON
file_path = '../assets/Material/material_brinklinks.json'

# Fonction pour convertir une couleur hexadécimale en RGB
def hex_to_rgb(hex_color):
    """
    Convert a hex color string to an RGB tuple.

    Args:
        hex_color (str): A string representing a hex color (e.g., '#RRGGBB').

    Returns:
        tuple: A tuple containing the RGB values (red, green, blue) as integers.

    Example:
        >>> hex_to_rgb('#FFFFFF')
        (255, 255, 255)
    """
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Fonction pour déterminer si une couleur est transparente
def is_transparent(color_type):
    """
    Check if the given color type is 'transparent'.

    Args:
        color_type (str): The color type to check.

    Returns:
        bool: True if the color type is 'transparent', False otherwise.
    """
    return color_type.lower() == 'transparent'

# Fonction pour ajouter les nouvelles valeurs et supprimer les anciennes
def reformat_data(data):
    """
    Reformats a list of dictionaries containing material data.

    Args:
        data (list): A list of dictionaries where each dictionary represents a material with keys 
                     and values containing material properties.

    Returns:
        dict: A dictionary where each key is a material identifier and the value is another dictionary 
              containing the reformatted material properties:
              - 'name' (str): The name of the material.
              - 'rgb' (tuple): The RGB color value converted from the hex color.
              - 'hex' (str): The hex color value prefixed with '#'.
              - 'metallic' (float): The metallic property of the material (0.2 for 'Solid' type, 0.8 otherwise).
              - 'roughness' (float): The roughness property of the material (0.5 for 'Solid' type, 0.3 otherwise).
              - 'transparent' (bool): Whether the material is transparent or not, determined by its type.
    """
    reformatted_data = {}
    for item in data:
        for key, value in item.items():
            hex_color = value['bgColor']
            colors = hex_to_rgb(hex_color)
            newColors = []
            for color in colors:
                newColors.append(round(color / 256, 2))
            reformatted_data[key] = {
                'name': value['name'],
                'rgb': newColors,
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
output_file = file_path.replace('material_brinklinks.json', 'reformatted_table_data.json')
with open(output_file, 'w') as file:
    json.dump(reformatted_data, file, indent=2)

print("Données reformattées et enregistrées avec succès.")