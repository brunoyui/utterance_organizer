from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .utterance_base import UtteranceBase
    from .paraphrase_user import ParaphraseUser
    from .utterance_domain import UtteranceDomain

class Paraphrase(Base):
    __tablename__ = "paraphrase"
    id = Column(String, primary_key=True, index=True)
    portuguese = Column(String)
    english = Column(String)
    classification = Column(String)
    domain = Column(String)
    concept = Column(String)

    utterance_base_id = Column(String, ForeignKey("utterance_base.id"))
    utterance_domain_id = Column(String, ForeignKey("utterance_domain.id"))

    utterance_base = relationship("UtteranceBase", back_populates="paraphrases")
    comments = relationship("ParaphraseUser", back_populates="paraphrase")
    utterance_domain = relationship("UtteranceDomain", back_populates="paraphrases")