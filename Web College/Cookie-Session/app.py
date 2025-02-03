from flask import Flask, request, make_response, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/set_cookie')
def set_cookie():
    response = make_response("Cookie has been set!")
    response.set_cookie("username", 'SepuhRega' )
    return response

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    if username:
        return f"Hello, {username}"
    return "No cookie found."

@app.route('/update_cookie')
def update_cookie():
    response = make_response("Cookie has been updated!")
    response.set_cookie("username", 'KingAmarLele')
    return response

@app.route('/delete_cookie')
def delete_cookie():
    response = make_response("Cookie has been deleted!")
    response.set_cookie('username', '', expires=0)
    return response

@app.route('/set_session')
def set_session():
    session['username'] = 'RepalGayrard'
    return "Session has been set!"

@app.route('/get_session')
def get_session():
    username = session.get('username')
    if username:
        return f"Hello, {username}!"
    return "No session data found."

@app.route('/update_session')
def update_session():
    if 'username' in session:
        session['username'] = 'JohanJomok'
        return 'Session has been updated!'
    return "No session data to update."

@app.route('/clear_session')
def clear_session():
    session.clear()
    return "Session has been cleared!"

if __name__=='__main__':
    app.run(debug=True)
