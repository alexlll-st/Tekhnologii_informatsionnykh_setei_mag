# This is a sample Python script.
from flask import Flask, request, jsonify
from extension import db
from models import Event


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # отключает лишние сигналы, экономит память
app.config['SQLALCHEMY_ECHO'] = True                   # печатать SQL-запросы в консоль (для отладки)
db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5002)
