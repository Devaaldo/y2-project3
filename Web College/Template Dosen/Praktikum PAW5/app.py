from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

items = {
    'laptop': 1200,
    'smartphone': 800,
    'headphones': 150,
    'tablet': 600,
}

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/purchase', methods=['POST'])
def purchase():
    data = request.get_json()
    item_name = data.get('item')
    quantity = data.get('quantity')

    if item_name in items and quantity > 0:
        price = items[item_name]
        total_cost = price * quantity
        return jsonify({
            'message': f'You successfully purchased {quantity} {item_name}(s) for ${total_cost}!',
            'total': total_cost        
        })
    
    return jsonify({'error': 'Invalid item or quantity!'}), 400

if __name__ == '__main__':
    app.run(debug=True)