from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .paraphrase import Paraphrase
    from .user import User

class ParaphraseUser(Base):
    __tablename__ = "paraphrase_user"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)

    paraphrase_id = Column(String, ForeignKey("paraphrase.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    paraphrase = relationship("Paraphrase", back_populates="comments")
    user = relationship("User", back_populates="comments_paraphrase")