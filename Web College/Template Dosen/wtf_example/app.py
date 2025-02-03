from flask import Flask, render_template, redirect, url_for, flash, request
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'

@app.route('/form_wtf', methods=['GET', 'POST'])
def form_wtf():
    form = ContactForm()
    if form.validate_on_submit():
        # Redirect to the submit_wtf route with the name and email passed as URL parameters
        return redirect(url_for('submit_wtf', name=form.name.data, email=form.email.data))
    return render_template('form_wtf.html', form=form)

# Define the submit_wtf route to handle GET requests
@app.route('/submit_wtf', methods=['GET'])
def submit_wtf():
    # Retrieve the name and email from the URL parameters
    name = request.args.get('name')
    email = request.args.get('email')
    
    # Flash a success message
    flash(f'Successfully submitted: {name}, {email}', 'success')
    
    # Render the submit_success.html template and pass the name and email
    return render_template('submit_success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
