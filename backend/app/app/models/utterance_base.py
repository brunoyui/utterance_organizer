from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .paraphrase import Paraphrase
    from .utterance_base_user import UtteranceBaseUser
    from .sql_declaration import SQLDeclaration
    from .utterance_domain import UtteranceDomain

class UtteranceBase(Base):
    __tablename__ = "utterance_base"
    id = Column(String, primary_key=True, index=True)
    portuguese = Column(String)
    english = Column(String)
    classification = Column(String)
    domain = Column(String)
    concept = Column(String)

    paraphrases = relationship("Paraphrase", back_populates="utterance_base")
    comments = relationship("UtteranceBaseUser", back_populates="utterance_base")
    sqls_declaration = relationship("SQLDeclaration", back_populates="utterance_base")
    utterance_domain = relationship("UtteranceDomain", back_populates="utterance_base")