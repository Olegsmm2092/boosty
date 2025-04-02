from pydantic import BaseModel, Field, validator
import re

class TicketModel(BaseModel):
    id: int
    title: str|None = Field(max_length=30, default=None)
    status: str = "Draft"
    type: str = Field(default='Bug', pattern=r'^Bug|Story|Epic$')
    severity: int = Field(default=0, ge=0, lt=10)

    @validator("type")
    def validate_type(cls, value):
        duplicate_last_letter_pattern = r'(\w)\1$'  # Checks if last letter is duplicated
        if re.search(duplicate_last_letter_pattern, value):
            raise ValueError(f"'{value}' contains a duplicate last letter.")
        return value

