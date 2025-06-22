# hbnb/app/models/amenity.py
from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        super().__init__(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data.update({"name": self.name})
        return data
