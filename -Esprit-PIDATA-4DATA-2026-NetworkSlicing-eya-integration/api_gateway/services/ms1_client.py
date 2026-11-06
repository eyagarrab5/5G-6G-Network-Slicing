"""
HTTP Client for MS-1 Prediction Service
Communicates with existing Flask app on port 5001
"""
import httpx
from typing import Dict, Any
from config import settings


class MS1Client:
    """Client for MS-1 Prediction Service"""
    
    def __init__(self):
        self.base_url = settings.MS1_URL
        self.timeout = settings.REQUEST_TIMEOUT
    
    async def predict_qos_6g(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Call MS-1 6G QoS prediction endpoint
        POST /predict/qos
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/predict/qos",
                    json=data
                )
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-1 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-1 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-1 returned error: {e.response.status_code}")
    
    async def predict_qos_5g(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Call MS-1 5G QoS prediction endpoint
        POST /predict/qos/5g
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/predict/qos/5g",
                    json=data
                )
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-1 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-1 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-1 returned error: {e.response.status_code}")
    
    async def predict_congestion(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Call MS-1 congestion prediction endpoint
        POST /predict/congestion
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/predict/congestion",
                    json=data
                )
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-1 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-1 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-1 returned error: {e.response.status_code}")
    
    async def get_prediction_history(self, limit: int = 50) -> Dict[str, Any]:
        """
        Call MS-1 prediction history endpoint
        GET /predict/history?limit=N
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(
                    f"{self.base_url}/predict/history",
                    params={"limit": limit}
                )
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-1 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-1 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-1 returned error: {e.response.status_code}")
    
    async def get_prediction_stats(self) -> Dict[str, Any]:
        """
        Call MS-1 prediction statistics endpoint
        GET /predict/stats
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.base_url}/predict/stats")
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-1 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-1 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-1 returned error: {e.response.status_code}")
    
    async def health_check(self) -> Dict[str, Any]:
        """
        Call MS-1 health check endpoint
        GET /health
        """
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.base_url}/health")
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            raise ConnectionError(f"Cannot connect to MS-1 at {self.base_url}")
        except httpx.TimeoutException:
            raise TimeoutError(f"MS-1 request timed out after {self.timeout}s")
        except httpx.HTTPStatusError as e:
            raise Exception(f"MS-1 returned error: {e.response.status_code}")
