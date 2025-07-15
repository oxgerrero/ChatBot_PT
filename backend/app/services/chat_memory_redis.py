import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import redis
import json
from typing import List
from app.models.message import HistoryItem
from app.core.config import settings

class ChatMemoryRedis:
    def __init__(self):
        self.r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

    def _key(self, session_id: str) -> str:
        return f"chat:{session_id}"

    def get_history(self, session_id: str) -> List[HistoryItem]:
        raw = self.r.lrange(self._key(session_id), 0, -1)
        return [HistoryItem(**json.loads(item)) for item in raw]

    def append(self, session_id: str, item: HistoryItem):
        self.r.rpush(self._key(session_id), json.dumps(item.dict()))

    def reset(self, session_id: str):
        self.r.delete(self._key(session_id))
