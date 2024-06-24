from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from permissions import is_admin, is_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypassword@localhost/sit331'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(80), nullable=False)

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    temperature = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    if not is_user("guest"):
        return "Access Denied"
    weathers = Weather.query.all()
    return render_template('index.html', weathers=weathers)

@app.route('/add', methods=['GET', 'POST'])
def add_weather():
    if not is_admin("admin"):
        return "Access Denied"
    if request.method == 'POST':
        city = request.form['city']
        temperature = request.form['temperature']
        new_weather = Weather(city=city, temperature=temperature)
        db.session.add(new_weather)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/delete/<int:id>')
def delete_weather(id):
    if not is_admin("admin"):
        return "Access Denied"
    weather = Weather.query.get(id)
    db.session.delete(weather)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
