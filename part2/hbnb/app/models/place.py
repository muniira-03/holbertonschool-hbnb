# hbnb/app/models/place.py
from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.city = kwargs.get("city", "")
        self.owner_id = kwargs.get("owner_id", "")
        self.price = kwargs.get("price", 0)
        self.latitude = kwargs.get("latitude", None)
        self.longitude = kwargs.get("longitude", None)
        self.amenities = kwargs.get("amenities", [])  # list of amenity IDs
        super().__init__(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "name": self.name,
            "city": self.city,
            "owner_id": self.owner_id,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "amenities": self.amenities
        })
        return datai
