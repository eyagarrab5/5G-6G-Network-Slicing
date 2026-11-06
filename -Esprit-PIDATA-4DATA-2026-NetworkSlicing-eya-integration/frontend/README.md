# React Frontend for Network Slicing Platform

Simple React dashboard for 5G/6G Network Slicing visualization.

## Installation

```bash
cd frontend
npm install
```

## Running

### Development

```bash
npm run dev
```

Server runs on http://localhost:3000

### Production Build

```bash
npm run build
npm run preview
```

## Features

- **Dashboard**: Network metrics visualization with charts
- **Prediction Form**: 5G/6G QoS prediction interface
- **Anomaly Detection**: Network anomaly detection interface

## Demo Data

When Flask services are unavailable, the frontend displays clearly labeled demo data.

## API Integration

The frontend connects to the FastAPI Gateway on port 8000 via proxy configuration.
