from extensions import db

class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    rate = db.Column(db.Float, nullable=False)
    tags = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable = False)
    theatre_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __init__(self, name, rate, tags, price, theatre_id):
        self.name = name
        self.rate = rate
        self.tags = tags
        self.price = price
        self.theatre_id = theatre_id