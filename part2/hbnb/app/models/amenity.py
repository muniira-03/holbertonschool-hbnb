# app/models/amenity.py
from app.models.base import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def __str__(self):
        return f"<Amenity {self.name} id={self.id}>"
