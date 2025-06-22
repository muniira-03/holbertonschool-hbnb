# hbnb/app/models/review.py
from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id", "")
        self.place_id = kwargs.get("place_id", "")
        self.text = kwargs.get("text", "")
        super().__init__(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "user_id": self.user_id,
            "place_id": self.place_id,
            "text": self.text
        })
        return data
