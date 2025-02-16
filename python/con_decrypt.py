import struct

file_path = '../assets/Ldraw/connectivity/3003.conn'

def read_conn_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    # Attempt to decode the binary data
    decoded_data = []
    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        if len(chunk) == 4:
            value = struct.unpack('f', chunk)[0]
            decoded_data.append(value)
    
    return decoded_data

def group_objects(decoded_data):
    # Assuming each object has 10 values
    object_size = 10
    grouped_objects = [decoded_data[i:i + object_size] for i in range(0, len(decoded_data), object_size)]
    
    # Organize objects based on their positions
    positions = {
        "bottom_left": grouped_objects[0],
        "bottom_right": grouped_objects[1],
        "bottom_center": grouped_objects[2],
        "bottom_top_left": grouped_objects[3],
        "bottom_top_right": grouped_objects[4],
        "top_left": grouped_objects[5],
        "top_right": grouped_objects[6],
        "top_center_left": grouped_objects[7],
        "top_center_right": grouped_objects[8]
    }
    
    return positions

def main():
    decoded_data = read_conn_file(file_path)
    
    # Group and organize the decoded data
    positions = group_objects(decoded_data)
    
    # Print the organized objects
    for position, obj in positions.items():
        print(f"{position.capitalize()}:")
        for value in obj:
            print(value)
        print()

if __name__ == "__main__":
    main()