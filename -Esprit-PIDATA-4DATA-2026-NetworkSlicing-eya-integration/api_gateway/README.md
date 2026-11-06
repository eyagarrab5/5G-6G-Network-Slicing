# FastAPI Gateway

API Gateway for the 5G/6G Network Slicing Platform. Acts as a Backend-for-Frontend (BFF) that proxies requests to existing Flask microservices.

## Architecture

```
React Frontend → FastAPI Gateway (8000) → Flask Services
                                          ├─ MS-1 (5001) - Predictions
                                          ├─ MS-2 (5000) - Anomalies
                                          └─ MS-3 (5003) - Dashboard
```

## Installation

```bash
cd api_gateway
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and configure service URLs:

```bash
cp .env.example .env
```

## Running

### Development

```bash
python main.py
```

Server runs on http://localhost:8000

API Documentation: http://localhost:8000/docs

### Production

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Testing

```bash
# Make sure Flask services are running first
python test_gateway.py
```

## API Endpoints

### Predictions (MS-1)
- `POST /api/v1/predictions/qos/6g` - 6G QoS prediction
- `POST /api/v1/predictions/qos/5g` - 5G QoS prediction
- `POST /api/v1/predictions/congestion` - Congestion prediction
- `GET /api/v1/predictions/history` - Prediction history
- `GET /api/v1/predictions/stats` - Prediction statistics

### Anomalies (MS-2)
- `POST /api/v1/anomalies/detect` - Detect anomaly
- `GET /api/v1/anomalies/history` - Anomaly history
- `GET /api/v1/anomalies/stats` - Anomaly statistics

### Dashboard (MS-3)
- `GET /api/v1/dashboard/data` - Dashboard data (slices + alerts)
- `POST /api/v1/dashboard/alerts/{id}/acknowledge` - Acknowledge alert

## Notes

- FastAPI does NOT connect directly to the database
- All data operations go through existing Flask services
- No authentication is implemented (as per requirements)
- No JWT or additional dependencies beyond what's needed
