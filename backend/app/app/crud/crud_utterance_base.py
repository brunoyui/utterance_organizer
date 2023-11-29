from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.utterance_base import UtteranceBase
from app.schemas.utterance_base import UtteranceBaseUpdate, UtteranceBaseUpdate

class CRUDUtteranceBase(CRUDBase[UtteranceBase, UtteranceBaseUpdate, UtteranceBaseUpdate]):
    def get_by_id(self, utterance_base_id: Any) -> UtteranceBase:
        utterance_base = crud.utterance_base.get(db, id=utterance_base_id)


utterance_base = CRUDUtteranceBase(UtteranceBase)