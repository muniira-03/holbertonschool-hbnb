from hbnb.app.models.db import db
from hbnb.app.models.associations import place_amenities

class Place(db.Model):
    __tablename__ = 'place'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))

    amenities = db.relationship(
        'Amenity',
        secondary=place_amenities,
        back_populates='places'
    )

    reviews = db.relationship('Review', back_populates='place')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "reviews": [review.to_dict() for review in self.reviews],
            "amenities": [amenity.to_dict() for amenity in self.amenities]
        }
