from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base_model import BaseModel


VALID_VOTE_TYPES = {"upvote", "downvote"}


@dataclass
class PostVote(BaseModel):
    vote_id: Optional[int] = None
    post_id: Optional[int] = None
    user_id: Optional[int] = None
    vote_type: Optional[str] = None
    created_at: Optional[datetime] = None

    def is_valid_vote_type(self):
        return self.vote_type in VALID_VOTE_TYPES


@dataclass
class CommentVote(BaseModel):
    vote_id: Optional[int] = None
    comment_id: Optional[int] = None
    user_id: Optional[int] = None
    vote_type: Optional[str] = None
    created_at: Optional[datetime] = None

    def is_valid_vote_type(self):
        return self.vote_type in VALID_VOTE_TYPES
