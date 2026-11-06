"""
Test script for FastAPI Gateway
Tests basic connectivity to Flask services
"""
import asyncio
import httpx


async def test_gateway():
    """Test FastAPI gateway endpoints"""
    base_url = "http://localhost:8000"
    
    print("Testing FastAPI Gateway...")
    print("=" * 50)
    
    async with httpx.AsyncClient() as client:
        # Test root endpoint
        try:
            response = await client.get(f"{base_url}/")
            print(f"✅ Root endpoint: {response.status_code}")
            print(f"   Response: {response.json()}")
        except Exception as e:
            print(f"❌ Root endpoint failed: {e}")
        
        # Test health endpoint
        try:
            response = await client.get(f"{base_url}/health")
            print(f"✅ Health endpoint: {response.status_code}")
            print(f"   Response: {response.json()}")
        except Exception as e:
            print(f"❌ Health endpoint failed: {e}")
        
        # Test predictions history
        try:
            response = await client.get(f"{base_url}/api/v1/predictions/history?limit=5")
            print(f"✅ Predictions history: {response.status_code}")
            data = response.json()
            print(f"   Total predictions: {data.get('total', 0)}")
        except Exception as e:
            print(f"❌ Predictions history failed: {e}")
        
        # Test predictions stats
        try:
            response = await client.get(f"{base_url}/api/v1/predictions/stats")
            print(f"✅ Predictions stats: {response.status_code}")
            print(f"   Response: {response.json()}")
        except Exception as e:
            print(f"❌ Predictions stats failed: {e}")
        
        # Test dashboard data
        try:
            response = await client.get(f"{base_url}/api/v1/dashboard/data")
            print(f"✅ Dashboard data: {response.status_code}")
            data = response.json()
            print(f"   Slices: {len(data.get('slices', []))}")
            print(f"   Alerts: {len(data.get('alerts', []))}")
        except Exception as e:
            print(f"❌ Dashboard data failed: {e}")
    
    print("=" * 50)
    print("Test complete!")


if __name__ == "__main__":
    asyncio.run(test_gateway())
