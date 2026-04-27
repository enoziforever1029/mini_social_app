from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base_model import BaseModel


VALID_FILE_TYPES = {"image", "video", "audio", "document", "other"}


@dataclass
class FileRecord(BaseModel):
    file_id: Optional[int] = None
    post_id: Optional[int] = None
    user_id: Optional[int] = None
    original_file_name: Optional[str] = None
    stored_file_name: Optional[str] = None
    file_type: Optional[str] = None
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    uploaded_at: Optional[datetime] = None

    def is_valid_file_type(self):
        return self.file_type in VALID_FILE_TYPES
