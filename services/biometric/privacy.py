from typing import Dict, Any


class BiometricPrivacyService:
    def __init__(self) -> None:
        self.dead_letter: list[dict[str, Any]] = []

    def pseudonymize(self, subject_token: str) -> str:
        return f"token_{subject_token[:12]}"

    def deidentify(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        clean = dict(payload)
        clean["subject_token"] = self.pseudonymize(clean.get("subject_token", "unknown"))
        clean.pop("device_id", None)
        clean.pop("raw_payload", None)
        return clean

    def validate(self, payload: Dict[str, Any]) -> bool:
        required = {"subject_token", "sensor_type", "value", "timestamp"}
        return required.issubset(payload.keys())

    def quarantine(self, payload: Dict[str, Any], reason: str) -> None:
        self.dead_letter.append({"payload": payload, "reason": reason})
