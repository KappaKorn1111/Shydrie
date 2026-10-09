from typing import Any, Dict


class RFFFTProcessor:
    def __init__(self) -> None:
        self.window_size = 4096

    def process(self, samples: list[float]) -> Dict[str, Any]:
        if not samples:
            return {"status": "empty", "spectrum": []}

        fft_values = [abs(v) for v in samples[: self.window_size]]
        return {
            "status": "processed",
            "fft_size": len(fft_values),
            "spectrum": fft_values,
        }
