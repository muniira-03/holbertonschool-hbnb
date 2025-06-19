# app/models/place.py
from app.models.base import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, location, owner_id, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.location = location
        self.owner_id = owner_id
        self.reviews = []
        self.amenities = []

    def __str__(self):
        return f"<Place {self.name} id={self.id}>"

