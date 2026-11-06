"""
HTTP Client for MS-3 Dashboard Service
Communicates with existing Flask app on port 5003
"""
import httpx
from typing import Dict, Any
from config import settings


class MS3Client:
    """Client for MS-3 Dashboard Service"""
    
    def __init__(self):
        self.base_url = settings.MS3_URL
        self.timeout = settings.REQUEST_TIMEOUT
    
    async def get_dashboard_slices(self) -> Dict[str, Any]:
        """
        Call MS-3 dashboard slices endpoint
        GET /dashboard/slices
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.base_url}/dashboard/slices")
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-3 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-3 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-3 returned error: {e.response.status_code}")
    
    async def get_dashboard_alerts(self) -> Dict[str, Any]:
        """
        Call MS-3 dashboard alerts endpoint
        GET /dashboard/alerts
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.base_url}/dashboard/alerts")
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-3 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-3 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-3 returned error: {e.response.status_code}")
    
    async def acknowledge_alert(self, alert_id: int) -> Dict[str, Any]:
        """
        Call MS-3 acknowledge alert endpoint
        POST /dashboard/alert/ack
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/dashboard/alert/ack",
                    json={"alert_id": alert_id}
                )
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-3 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-3 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-3 returned error: {e.response.status_code}")
