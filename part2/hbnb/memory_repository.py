import uuid
from copy import deepcopy

class MemoryRepository:
    def __init__(self):
        self.users = {}

    def get_all_users(self):
        return list(self.users.values())

    def create_user(self, data):
        user_id = str(uuid.uuid4())
        user = {
            'id': user_id,
            'email': data.get('email'),
            'password': data.get('password'),
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
        }
        self.users[user_id] = user
        return deepcopy(user)

    def get_user_by_id(self, user_id):
        user = self.users.get(user_id)
        if user:
            return deepcopy(user)
        return None

    def update_user(self, user_id, data):
        user = self.users.get(user_id)
        if not user:
            return None
        user.update(data)
        return deepcopy(user)

