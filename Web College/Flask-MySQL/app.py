from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'secret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sql123'  # Gantikan dengan password anda
app.config['MYSQL_DB'] = 'flight_db'

mysql = MySQL(app)

# Initialize database
@app.route('/init_db')
def init_db():
    cursor = mysql.connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flights (
                        flight_id INT AUTO_INCREMENT PRIMARY KEY,
                        flight_name VARCHAR(255) NOT NULL,
                        origin VARCHAR(255) NOT NULL,
                        destination VARCHAR(255) NOT NULL
                        );''')
    # nama column, datatype, sifat (khusus primary id), set null
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        booking_id INT AUTO_INCREMENT PRIMARY KEY,
                        flight_id INT,
                        passenger_name VARCHAR(255) NOT NULL,
                        FOREIGN KEY (flight_id) REFERENCES flights(flight_id) ON DELETE CASCADE
                        );''')
    mysql.connection.commit()
    cursor.close()
    return 'Database Initialized!'


# Read: Display all flights with bookings
@app.route('/')
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('''
        SELECT flights.flight_id, flights.flight_name, flights.origin, flights.destination,
            bookings.booking_id, bookings.passenger_name
        FROM flights
        LEFT JOIN bookings ON flights.flight_id = bookings.flight_id
    ''')
    flights = cursor.fetchall()
    cursor.close()
    return render_template('index.html', flights=flights)


# Insert: Add a new flight
@app.route('/add_flight', methods=['GET', 'POST'])
def add_flight():
    if request.method == 'POST':
        flight_name = request.form['flight_name']
        origin = request.form['origin']
        destination = request.form['destination']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO flights (flight_name, origin, destination) VALUES (%s, %s, %s)', (flight_name, origin, destination))
        mysql.connection.commit()
        cursor.close()
        flash('Flight added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_flight.html')


# Update: Edit an existing flight
@app.route('/update_flight/<int:flight_id>', methods=['GET', 'POST'])
def update_flight(flight_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM flights WHERE flight_id = %s', (flight_id,))
    flight = cursor.fetchone()
    cursor.close()

    if request.method == 'POST':
        flight_name = request.form['flight_name']
        origin = request.form['origin']
        destination = request.form['destination']
        
        cursor = mysql.connection.cursor()
        cursor.execute('''
            UPDATE flights
            SET flight_name = %s, origin = %s, destination = %s
            WHERE flight_id = %s
        ''', (flight_name, origin, destination, flight_id))
        mysql.connection.commit()
        cursor.close()
        flash('Flight updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('update_flight.html', flight=flight)


# Delete: Remove a flight
@app.route('/delete_flight/<int:flight_id>')
def delete_flight(flight_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM flights WHERE flight_id = %s', (flight_id,))
    mysql.connection.commit()
    cursor.close()
    flash('Flight deleted successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
