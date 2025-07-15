from app.services.chat_memory_redis import ChatMemoryRedis
from app.models.message import HistoryItem 

def test_memory_save_and_get():
    memory = ChatMemoryRedis()

    session_id = "session123"
    message = HistoryItem(role="user", content="Hola") 
    
    class DummyRedis:
        store = {}
        def rpush(self, key, value):
            self.store.setdefault(key, []).append(value)
        def lrange(self, key, start, end):
            return self.store.get(key, [])
    memory.r = DummyRedis()

    memory.append(session_id, message)
    history = memory.get_history(session_id)

    assert len(history) == 1
    assert history[0].role == "user"
    assert history[0].content == "Hola"