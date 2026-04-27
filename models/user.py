from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base_model import BaseModel


@dataclass
class User(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    display_name: Optional[str] = None
    bio: Optional[str] = None
    profile_picture_path: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def public_dict(self):
        """Return user data that is safe to show in UI or future API responses."""
        data = self.to_dict()
        data.pop("password_hash", None)
        return data

    def __str__(self):
        return f"User({self.user_id}, {self.username}, {self.email})"
