from collections import defaultdict
import time

_requests = defaultdict(list)


def check_rate_limit(user_id: str, limit: int = 60):
    now = time.time()
    _requests[user_id] = [x for x in _requests[user_id] if now - x < 60]

    if len(_requests[user_id]) >= limit:
        return False

    _requests[user_id].append(now)
    return True
