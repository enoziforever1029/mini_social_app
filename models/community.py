from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base_model import BaseModel


@dataclass
class Community(BaseModel):
    community_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    created_by: Optional[int] = None
    created_at: Optional[datetime] = None
