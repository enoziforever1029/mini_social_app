from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base_model import BaseModel


@dataclass
class Comment(BaseModel):
    comment_id: Optional[int] = None
    post_id: Optional[int] = None
    user_id: Optional[int] = None
    parent_comment_id: Optional[int] = None
    content: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @property
    def is_reply(self):
        return self.parent_comment_id is not None
