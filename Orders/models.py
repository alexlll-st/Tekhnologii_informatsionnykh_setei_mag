from extension import db
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prise = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(120), nullable=False)
class Product(db.Model):         # явное имя таблицы (иначе было бы 'user')
    id    = db.Column(db.Integer, primary_key=True)
    id_order = db.Column(db.Integer)
    name  = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False, index=True)
    prise   = db.Column(db.Integer, default=0)
    stoack = db.Column(db.Integer, primary_key=True)
