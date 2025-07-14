from hbnb.app.models.db import db

place_amenities = db.Table('place_amenities',
    db.Column('place_id', db.Integer, db.ForeignKey('place.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenity.id'), primary_key=True)
)
