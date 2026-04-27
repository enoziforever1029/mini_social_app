from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base_model import BaseModel


@dataclass
class SavedPost(BaseModel):
    saved_id: Optional[int] = None
    post_id: Optional[int] = None
    user_id: Optional[int] = None
    saved_at: Optional[datetime] = None
