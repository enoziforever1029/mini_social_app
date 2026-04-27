from dataclasses import asdict, fields
from datetime import date, datetime
from decimal import Decimal
from enum import Enum


class BaseModel:
    """Shared helper methods for all model/data classes."""

    @classmethod
    def from_db_row(cls, row):
        """
        Convert a database dictionary row into a model instance.
        Works with mysql.connector cursors using dictionary=True.
        """
        if row is None:
            return None

        allowed_fields = {field.name for field in fields(cls)}
        cleaned_row = {
            key: value
            for key, value in dict(row).items()
            if key in allowed_fields
        }
        return cls(**cleaned_row)

    def to_dict(self, include_none=True):
        """Convert model data into a regular dictionary."""
        data = asdict(self)

        if not include_none:
            data = {key: value for key, value in data.items() if value is not None}

        return {key: self._serialize_value(value) for key, value in data.items()}

    @staticmethod
    def _serialize_value(value):
        """Make values safe for JSON responses, logs, and future API use."""
        if isinstance(value, (datetime, date)):
            return value.isoformat()
        if isinstance(value, Decimal):
            return float(value)
        if isinstance(value, Enum):
            return value.value
        return value
