from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .paraphrase import Paraphrase
    from .utterance_domain_user import UtteranceDomainUser
    from .sql_declaration import SQLDeclaration

class UtteranceDomain(Base):
    __tablename__ = "utterance_domain"
    id = Column(String, primary_key=True, index=True)
    portuguese = Column(String)
    english = Column(String)
    classification = Column(String)
    domain = Column(String)
    concept = Column(String)

    utterance_base_id = Column(Integer, ForeignKey("utterance_base.id"))

    utterance_base = relationship("UtteranceBase", back_populates="utterance_domain")
    paraphrases = relationship("Paraphrase", back_populates="utterance_domain")
    comments = relationship("UtteranceDomainUser", back_populates="utterance_domain")
    sqls_declaration = relationship("SQLDeclaration", back_populates="utterance_domain")