from flask import Flask, jsonify, request

app = Flask(__name__)

# In memory data storage (like a database)

items = [
    {"id": 1, "name": "Item1", "price": 10.99},
    {"id": 2, "name": "Item2", "price": 19.99}
]

# GET route to fetch all items

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Get route to fetch a single item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"message": "Item not found"}), 484

# POST route to add a new item using form-data
@app.route('/items', methods=['POST'])
def add_items():
    # Get data from form-data
    name = request.form.get("name")
    price = request.form.get("price")

    if not name or not price:
        return jsonify({"message": "Missing name or price"}), 400
    
    try:
        price = float(price) # Convert price to float
    except ValueError:
        return jsonify({"message": "Price should be a valid number"}), 400
    
    new_item = {
        "id": len(items) + 1,
        "name": name,
        "price": price
    }

    items.append(new_item)
    return jsonify(new_item), 201

# PUT route to update an tem using form -data
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"message": "Item not found"}), 484
    
    # Get data from form-data
    name = request.form.get("name", item['name'])
    price = request.form.get("price", item['price'])

    try:
        price = float(price)
    except ValueError:
        return jsonify({"message": "Price should be a valid number"}), 400

    item['name'] = name
    item['price'] = price

    return jsonify(item), 200    

# DELETE route to delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)