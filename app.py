
from flask import Flask, jsonify

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
    }
]

@app.route('/api/animals', methods=['GET'])
def get_animals():
    return jsonify(animals)

if __name__ == '__main__':
    app.run(debug=True)

