# 5G/6G Network Slicing Platform

A microservices-based platform for 5G/6G network slicing: QoS prediction, real-time anomaly detection, and a NOC dashboard with alerting.

## Architecture

```
React Frontend (80)
      │
FastAPI Gateway / BFF (8000)
      │
      ├── MS-1: Prediction Service (5001)   — Flask, QoS/congestion ML models
      ├── MS-2: Anomaly Detection (5000)     — Flask, Isolation Forest + Autoencoder consensus
      ├── MS-3: Dashboard & Alerts (5003)    — Flask, slice state + alert management
      ├── MS-5: Model Management (5005)      — Flask, model versioning
      └── MySQL 8.0 (3306)                   — shared database
```

## Services

| Service | Port | Description | Docs |
|---------|------|-------------|------|
| `ms1` (root `app.py`) | 5001 | QoS & congestion prediction | — |
| `anomaly/` | 5000 | Anomaly detection (IF + Autoencoder) | [README](anomaly/README_MS2.md) |
| `ms3/` | 5003 | Dashboard, alerts, thresholds | [README](ms3/README.md) |
| `ms5_model_management/` | 5005 | ML model version management | — |
| `api_gateway/` | 8000 | FastAPI gateway / BFF | [README](api_gateway/README.md) |
| `frontend/` | 80 | React dashboard (nginx) | [README](frontend/README.md) |

## Quick Start

Requires Docker and Docker Compose.

```bash
docker compose up -d --build
```

Then open:

- **Frontend**: http://localhost
- **API Gateway docs**: http://localhost:8000/docs
- **MS-3 dashboard**: http://localhost:5003 (login: `admin` / `admin`)

## Tech Stack

- **Backend**: Python, Flask, Flask-SQLAlchemy, FastAPI, Uvicorn
- **ML**: scikit-learn (Isolation Forest, Autoencoder), joblib
- **Frontend**: React, Vite, Recharts
- **Database**: MySQL 8.0
- **Infra**: Docker, Docker Compose, nginx

## Project Structure

```
├── ms1/                           # MS-1 prediction service
├── anomaly/                       # MS-2 anomaly detection
├── ms3/                           # MS-3 dashboard & alerts
├── ms5_model_management/          # MS-5 model management
├── api_gateway/                   # FastAPI gateway
├── frontend/                      # React frontend
├── docker-compose.yml             # Full stack orchestration
└── README.md                      # This file
```

## License

Academic project.
