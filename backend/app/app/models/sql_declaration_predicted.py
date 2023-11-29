from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .sql_declaration import SQLDeclaration

class SQLDeclarationPredicted(Base):
    __tablename__ = "sql_declaration_predicted"
    id = Column(Integer, primary_key=True, index=True)
    sql_command = Column(String)
    model = Column(String)

    sql_declaration_id = Column(Integer, ForeignKey("sql_declaration.id"))

    sql_declaration = relationship("SQLDeclaration", back_populates="sqls_declaration_predicted")

