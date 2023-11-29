from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .sqls_declaration_predicted import SQLDeclarationPredicted
    from .utterance_base import UtteranceBase
    from .utterance_domain import UtteranceDomain

class SQLDeclaration(Base):
    __tablename__ = "sql_declaration"
    id = Column(Integer, primary_key=True, index=True)
    sql_command = Column(String)
    indicator = Column(String)
    classification = Column(String)
    database = Column(String)

    utterance_base_id = Column(Integer, ForeignKey("utterance_base.id"))
    utterance_domain_id = Column(Integer, ForeignKey("utterance_domain.id"))

    sqls_declaration_predicted = relationship("SQLDeclarationPredicted", back_populates="sql_declaration")
    utterance_base = relationship("UtteranceBase", back_populates="sqls_declaration")
    utterance_domain = relationship("UtteranceDomain", back_populates="sqls_declaration")
