"""
HTTP Client for MS-2 Anomaly Detection Service
Communicates with existing Flask app on port 5000
"""
import httpx
from typing import Dict, Any, Optional
from config import settings


class MS2Client:
    """Client for MS-2 Anomaly Detection Service"""
    
    def __init__(self):
        self.base_url = settings.MS2_URL
        self.timeout = settings.REQUEST_TIMEOUT
    
    async def detect_anomaly(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Call MS-2 anomaly detection endpoint
        POST /api/anomaly/detect
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/anomaly/detect",
                    json=data
                )
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-2 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-2 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-2 returned error: {e.response.status_code}")
    
    async def get_anomaly_history(
        self,
        slice_id: Optional[str] = None,
        is_anomaly: Optional[bool] = None,
        method: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> Dict[str, Any]:
        """
        Call MS-2 anomaly history endpoint
        GET /api/anomaly/history
        """
        try:
            params = {
                "limit": limit,
                "offset": offset
            }
            if slice_id:
                params["slice_id"] = slice_id
            if is_anomaly is not None:
                params["is_anomaly"] = str(is_anomaly).lower()
            if method:
                params["method"] = method
            if start_date:
                params["start_date"] = start_date
            if end_date:
                params["end_date"] = end_date
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/api/anomaly/history",
                    params=params
                )
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-2 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-2 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-2 returned error: {e.response.status_code}")
    
    async def get_anomaly_stats(
        self,
        slice_id: Optional[str] = None,
        period: str = "jour",
        days: int = 7
    ) -> Dict[str, Any]:
        """
        Call MS-2 anomaly statistics endpoint
        GET /api/anomaly/stats
        """
        try:
            params = {
                "period": period,
                "days": days
            }
            if slice_id:
                params["slice_id"] = slice_id
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/api/anomaly/stats",
                    params=params
                )
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-2 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-2 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-2 returned error: {e.response.status_code}")
