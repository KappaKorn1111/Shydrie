from datetime import datetime
from typing import Any, Dict


class TelemetryService:
    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def emit_event(self, event_type: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            **metadata,
        }
        self.events.append(event)
        return event

    def list_events(self) -> list[dict[str, Any]]:
        return self.events
