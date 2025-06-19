# app/models/user.py
from app.services.facade import create_user, get_user_by_id, get_all_users, update_user

class User(BaseModel):
    def __init__(self, username, email, password, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.email = email
        self.password = password
        self.places = []

    def __str__(self):
        return f"<User {self.username} id={self.id}>"

