from flask_bcrypt import Bcrypt
from datetime import datetime
import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from hbnb.app.models.base import Base
bcrypt = Bcrypt()

class User(Base):
    __tablename__ = 'users'

    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(128), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.set_password(password)
        self.is_admin = is_admin

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

