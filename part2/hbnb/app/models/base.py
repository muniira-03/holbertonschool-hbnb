# app/models/base.py
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = id if id else str(uuid.uuid4())
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def update(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return f"<{self.__class__.__name__} id={self.id}>"

