from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/')
def home():
 return render_template('home.html')
@app.route('/welcome/<username>')
def welcome(username):
 return render_template('welcome.html', username=username)
@app.route('/submit', methods=['POST'])
def submit():
 name = request.form['username'] # Get the input from form
 if name:
     return redirect(url_for('welcome', username=name)) 
 return redirect(url_for('home'))
if __name__ == '__main__':
 app.run(debug=True)