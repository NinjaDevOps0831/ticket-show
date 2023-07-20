from extensions import db

class Theatre(db.Model):
    __tablename__ = 'theatres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    place = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(128), nullable=False)
    # image = db.Column(db.LargeBinary)
    
    def __init__(self, name, place, capacity, image):
        self.name = name
        self.place = place
        self.capacity = capacity
        self.image = image