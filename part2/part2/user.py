# hbnb/app/models/user.py
from .base_model import BaseModel

class User(BaseModel):
    def __init__(self, **kwargs):
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
        self.name = kwargs.get("name", "")
        super().__init__(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "email": self.email,
            "name": self.name
        })
        return data
