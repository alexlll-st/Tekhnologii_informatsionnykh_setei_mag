from extension import db
class Event(db.Model):         # явное имя таблицы (иначе было бы 'user')
    id    = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(120), nullable=False)
    order_id  = db.Column(db.Integer)
    customer_id = db.Column(db.Integer)
    created_all = db.Column(db.Date)