from datetime import datetime

from pydantic import BaseModel


class AuditEvent(BaseModel):
    audit_id: str
    actor_id: str
    action: str
    resource_type: str
    resource_id: str
    policy_id: str
    decision: str
    timestamp: datetime
    source_ip: str
    auth_context: str
    before_state_hash: str
    after_state_hash: str
