from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base_model import BaseModel


VALID_POST_TYPES = {"text", "image", "video", "document", "link", "mixed"}


@dataclass
class Post(BaseModel):
    post_id: Optional[int] = None
    user_id: Optional[int] = None
    community_id: Optional[int] = None
    title: Optional[str] = None
    content: Optional[str] = None
    post_type: str = "text"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def is_valid_post_type(self):
        return self.post_type in VALID_POST_TYPES
