from hbnb.app.models.db import db

place_amenities = db.Table('place_amenities',
    db.Column('place_id', db.Integer, db.ForeignKey('place.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenity.id'), primary_key=True),
    extend_existing=True 
)

class Amenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    places = db.relationship('Place', secondary=place_amenities, backref='amenities')
