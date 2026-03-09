"""Timer utility for timed questions."""

import time
import threading


class QuestionTimer:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.start_time = None
        self.expired = False
        self._timer_thread = None

    def start(self):
        self.start_time = time.time()
        self.expired = False
        self._timer_thread = threading.Timer(self.time_limit, self._on_expire)
        self._timer_thread.daemon = True
        self._timer_thread.start()

    def _on_expire(self):
        self.expired = True

    def stop(self):
        if self._timer_thread:
            self._timer_thread.cancel()
        elapsed = time.time() - self.start_time if self.start_time else 0
        return elapsed

    def remaining(self):
        if self.start_time is None:
            return self.time_limit
        elapsed = time.time() - self.start_time
        return max(0, self.time_limit - elapsed)

    def is_expired(self):
        return self.expired
