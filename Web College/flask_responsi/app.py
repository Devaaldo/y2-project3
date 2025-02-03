from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data storage (like a database)
items = [
    {"id": 1, "name": "Item1", "price": 10.99},
    {"id": 2, "name": "Item2", "price": 19.99},
]

# Tampilkan semua data dari data Items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Tampilkan data berdasarkan ID dari data Items
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is not None:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

# Menambahkan data ke dalam data Items
@app.route('/items', methods=['POST'])
def add_item():
    if not request.json or 'name' not in request.json or 'price' not in request.json:
        return jsonify({"error": "Bad request, 'name' and 'price' are required"}), 400
    
    new_item = {
        "id" : items[-1]['id'] + 1 if items else 1,
        "name" : request.json['name'],
        "price" : request.json['price'] 
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Edit data dalam Items berdasarkan ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error" : "Item not Found"}), 404

    if not request.json:
        return jsonify({"error": "Bad request, JSON body is requeired"}), 404
    
    item['name'] = request.json.get('name', item['name'])
    item['price'] = request.json.get('price', item['price'])
    return jsonify(item), 200
    

# Menghapus data dalam Items
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    items.remove(item)
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
