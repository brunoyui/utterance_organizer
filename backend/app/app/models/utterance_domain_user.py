from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .utterance_domain import UtteranceDomain
    from .user import User

class UtteranceDomainUser(Base):
    __tablename__ = "utterance_domain_user"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    utterance_domain_id = Column(Integer, ForeignKey("utterance_domain.id"))

    utterance_domain = relationship("UtteranceDomain", back_populates="comments")
    user = relationship("User", back_populates="comments_utterance_domain")