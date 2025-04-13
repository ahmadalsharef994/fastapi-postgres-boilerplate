# --- api_gateway/events/event_bus.py ---
import asyncio
from collections import defaultdict

class EventBus:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_type, listener):
        self.listeners[event_type].append(listener)

    async def publish(self, event_type, data):
        if event_type in self.listeners:
            await asyncio.gather(*[listener(data) for listener in self.listeners[event_type]])

event_bus = EventBus()
