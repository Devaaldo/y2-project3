from flask import Flask, render_template, redirect, url_for
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('welcome', username=form.username.data))
    return render_template('register.html', form=form)

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)

