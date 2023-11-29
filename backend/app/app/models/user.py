from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .utterance_domain_user import UtteranceDomainUser
    from .utterance_base_user import UtteranceBaseUser
    from .paraphrase_user import ParaphraseUser

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    comments_utterance_domain = relationship("UtteranceDomainUser", back_populates="user")
    comments_utterance_base = relationship("UtteranceBaseUser", back_populates="user")
    comments_paraphrase = relationship("ParaphraseUser", back_populates="user")
