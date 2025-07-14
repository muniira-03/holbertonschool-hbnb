from hbnb.app.models.db import db

place_amenities = db.Table('place_amenities',
    db.Column('place_id', db.Integer, db.ForeignKey('place.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenity.id'), primary_key=True)
)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='places')
    reviews = db.relationship('Review', back_populates='place', cascade='all, delete-orphan')
    amenities = db.relationship('Amenity', secondary=place_amenities, backref='places')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "user_id": self.user_id,
            "reviews": [review.to_dict() for review in self.reviews],
            "amenities": [amenity.to_dict() for amenity in self.amenities],
        }
