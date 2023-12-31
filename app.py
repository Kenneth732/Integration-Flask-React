
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
animals = [
    {
        "name": "Lion",
        "image": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1159&q=80",
        "type": "Male",
        "weight": 280
    },
    {
        "name": "Tiger",
        "image": "https://plus.unsplash.com/premium_photo-1664302954356-a79b02fe66b8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1168&q=80",
        "type": "Female",
        "weight": 230
    },
    {
        "name": "Snow Fox",
        "image": "https://images.unsplash.com/photo-1474511320723-9a56873867b5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1172&q=80",
        "type": "Female",
        "weight": 23
    },
    {
        "name": "Snow Fox",
        "image": "https://cdn.pixabay.com/photo/2021/03/03/14/55/rhino-6065480_1280.jpg",
        "type": "Female",
        "weight": 23
    },
        {
        "name": "Elephant",
        "image": "https://images.unsplash.com/photo-1603483080228-04f2313d9f10?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1965&q=80",
        "type": "Female",
        "weight": 23
    },
            {
        "name": "Leopart",
        "image": "https://plus.unsplash.com/premium_photo-1664304400278-8152cba3da20?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1188&q=80",
        "type": "Female",
        "weight": 70
    }
]

@app.route('/api/animals', methods=['GET'])
def get_animals():
    return jsonify(animals)

@app.route('/api/animals', methods=['POST'])
def add_animal():
    # Handle the POST request here, and add the new animal to your data
    new_animal = request.json  # Assuming the new animal data is sent in JSON format
    animals.append(new_animal)  # Add the new animal to your data
    return jsonify(new_animal), 201  # Return the newly added animal with a 201 status code

@app.route('/api/animals/<int:index>', methods=['PUT'])
def edit_animal(index):
    # Get the updated animal data from the request
    updated_animal = request.json

    # Update the animal data at the specified index
    if 0 <= index < len(animals):
        animals[index] = updated_animal
        return jsonify(updated_animal), 200
    else:
        return jsonify({"error": "Animal not found"}), 404

@app.route('/api/animals/<int:index>', methods=['DELETE'])
def delete_animal(index):
    # Delete the animal at the specified index
    if 0 <= index < len(animals):
        deleted_animal = animals.pop(index)
        return jsonify(deleted_animal), 200
    else:
        return jsonify({"error": "Animal not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)

