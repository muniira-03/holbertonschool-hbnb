# app/models/review.py
from app.models.base import BaseModel

class Review(BaseModel):
    def __init__(self, user_id, place_id, rating, comment, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"<Review {self.id} rating={self.rating}>"
