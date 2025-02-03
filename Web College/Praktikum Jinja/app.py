from flask import Flask, render_template

app = Flask(__name__)

# Sample data to be used dynamically

users = [
    {'name': 'Alice', 'age': 30, 'location': 'New York'},
    {'name': 'Bob', 'age': 25, 'location': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'location': 'Chicago'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def list_users():
    return render_template('users.html', users=users)

if __name__== "__main__":
    app.run(debug=True)

