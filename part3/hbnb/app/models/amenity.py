from hbnb.app.models.db import db
from hbnb.app.models.associations import place_amenities

class Amenity(db.Model):
    __tablename__ = 'amenity'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    places = db.relationship(
        'Place',
        secondary=place_amenities,
        back_populates='amenities'
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
