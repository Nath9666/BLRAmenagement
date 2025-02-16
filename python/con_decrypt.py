import struct
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file_path = '../assets/Ldraw/connectivity/3003.conn'

def read_conn_file(file_path):
    """Lecture du fichier .conn et extraction des connexions"""
    with open(file_path, 'rb') as file:
        data = file.read()

    connection_size = 8
    format_string = 'ii6f'  # 2 entiers + 6 flottants

    num_connections = len(data) // struct.calcsize(format_string)
    connections = []
    
    for i in range(num_connections):
        chunk = data[i * struct.calcsize(format_string):(i + 1) * struct.calcsize(format_string)]
        values = struct.unpack(format_string, chunk)
        connections.append(values)

    return connections

def clean_connections(connections):
    """Nettoie les valeurs erronées et arrondit les coordonnées"""
    cleaned = []
    seen = set()  # Pour éviter les doublons

    for conn in connections:
        _, _, x, y, z, _, _, _ = conn

        # Arrondi pour éviter les erreurs numériques
        x, y, z = round(x, 3), round(y, 3), round(z, 3)

        # Ignorer les valeurs quasi nulles
        if abs(x) < 1e-5 and abs(y) < 1e-5 and abs(z) < 1e-5:
            continue

        # Éviter les doublons
        if (x, y, z) not in seen:
            seen.add((x, y, z))
            cleaned.append((x, y, z))

    return cleaned

def print_connections(connections):
    """Affichage des connexions après nettoyage"""
    print("\n--- Connexions après nettoyage ---")
    for i, (x, y, z) in enumerate(connections):
        print(f"{i+1}: X={x}, Y={y}, Z={z}")

def visualize_connections(connections):
    """Visualisation des connexions en 3D"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_vals, y_vals, z_vals = zip(*connections)
    
    ax.scatter(x_vals, y_vals, z_vals, c='red', marker='o', s=100)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Visualisation des points de connexion LEGO')

    plt.show()

def main():
    connections = read_conn_file(file_path)
    cleaned_connections = clean_connections(connections)

    print(f"Nombre de connexions après nettoyage : {len(cleaned_connections)}")

    # Affichage des coordonnées propres
    print_connections(cleaned_connections)

    # Visualisation
    visualize_connections(cleaned_connections)

if __name__ == "__main__":
    main()
