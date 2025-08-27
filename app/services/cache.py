import redis
import json
from typing import Optional
from app.config import REDIS_HOST, REDIS_PORT, REDIS_DB

redis_client = redis.Redis(
    host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True
)

def get_cache(key: str) -> Optional[dict]:
    """Fetch value from Redis, return None if not found or error."""
    try:
        cached_value = redis_client.get(key)
        return json.loads(cached_value) if cached_value else None
    except redis.exceptions.RedisError:
        return None

def set_cache(key: str, value: dict, ttl: int = 300) -> None:
    """Store value in Redis with TTL. Fail silently if Redis is unavailable."""
    try:
        redis_client.setex(key, ttl, json.dumps(value))
    except redis.exceptions.RedisError:
        pass
