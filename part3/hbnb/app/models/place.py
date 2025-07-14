from hbnb.app.models.db import db

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='places')
    reviews = db.relationship('Review', backref='place', cascade='all, delete-orphan')
