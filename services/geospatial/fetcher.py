from typing import Any, Dict


class GeospatialFetcher:
    def __init__(self, base_url: str = "https://data.noaa.gov") -> None:
        self.base_url = base_url

    def discover_granules(self, region: str, start: str, end: str) -> list[Dict[str, Any]]:
        return [
            {
                "granule_id": f"{region}-{start}-001",
                "provider": "NOAA",
                "platform": "NOAA-20",
                "status": "discovered",
                "start": start,
                "end": end,
            }
        ]

    def validate_metadata(self, granule: Dict[str, Any]) -> bool:
        return "granule_id" in granule and "provider" in granule
