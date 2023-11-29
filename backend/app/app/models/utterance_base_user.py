from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .utterance_base import UtteranceBase
    from .user import User

class UtteranceBaseUser(Base):
    __tablename__ = "utterance_base_user"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    utterance_base_id = Column(Integer, ForeignKey("utterance_base.id"))

    utterance_base = relationship("UtteranceBase", back_populates="comments")
    user = relationship("User", back_populates="comments_utterance_base")