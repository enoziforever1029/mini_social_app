from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base_model import BaseModel


VALID_COMMUNITY_ROLES = {"member", "moderator", "admin"}


@dataclass
class CommunityMember(BaseModel):
    member_id: Optional[int] = None
    community_id: Optional[int] = None
    user_id: Optional[int] = None
    role: str = "member"
    joined_at: Optional[datetime] = None

    def is_valid_role(self):
        return self.role in VALID_COMMUNITY_ROLES
