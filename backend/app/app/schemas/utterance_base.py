from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UtteranceBase(BaseModel):
    id: str = None
    portuguese: Optional[str] = None
    english: Optional[str] = None
    classification: Optional[str] = None
    domain: Optional[str] = None
    concept: Optional[str] = None

# Properties to receive via API on creation
class UtteranceBaseCreate(UtteranceBase):
    pass


# Properties to receive via API on update
class UtteranceBaseUpdate(UtteranceBase):
    pass