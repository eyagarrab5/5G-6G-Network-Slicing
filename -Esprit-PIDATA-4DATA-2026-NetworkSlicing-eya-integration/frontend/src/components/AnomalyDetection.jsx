import React, { useState } from 'react'
import { AlertTriangle, CheckCircle, XCircle } from 'lucide-react'
import './AnomalyDetection.css'

function AnomalyDetection() {
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const [features, setFeatures] = useState({
    bandwidth: 85.5,
    latency: 12.3,
    jitter: 2.1,
    packet_loss: 0.01
  })

  const handleDetect = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch('/api/v1/anomalies/detect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          slice_id: 'demo_slice_001',
          features: features
        })
      })

      if (!response.ok) {
        throw new Error(`HTTP ${response.status_code}`)
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      console.error('Anomaly detection failed:', err)
      setError('Unable to connect to anomaly detection service. Showing demo result.')
      setResult(getDemoResult())
    } finally {
      setLoading(false)
    }
  }

  const getDemoResult = () => ({
    is_anomaly: false,
    score: 0.23,
    confidence: 0.77,
    method: 'consensus',
    anomaly_id: null,
    methods: {
      isolation_forest: { is_anomaly: false, score: 0.21 },
      autoencoder: { is_anomaly: false, score: 0.25 }
    },
    _demo: true
  })

  const handleChange = (e) => {
    setFeatures({
      ...features,
      [e.target.name]: parseFloat(e.target.value)
    })
  }

  return (
    <div className="anomaly-detection">
      <div className="form-header">
        <AlertTriangle size={28} />
        <div>
          <h2>Anomaly Detection</h2>
          <p>Detect network anomalies using consensus algorithm (Demo Mode)</p>
        </div>
      </div>

      <form onSubmit={handleDetect} className="form">
        <div className="form-grid">
          <div className="form-group">
            <label>Bandwidth (Mbps)</label>
            <input
              type="number"
              name="bandwidth"
              value={features.bandwidth}
              onChange={handleChange}
              min="0"
              step="0.1"
            />
          </div>

          <div className="form-group">
            <label>Latency (ms)</label>
            <input
              type="number"
              name="latency"
              value={features.latency}
              onChange={handleChange}
              min="0"
              step="0.1"
            />
          </div>

          <div className="form-group">
            <label>Jitter (ms)</label>
            <input
              type="number"
              name="jitter"
              value={features.jitter}
              onChange={handleChange}
              min="0"
              step="0.1"
            />
          </div>

          <div className="form-group">
            <label>Packet Loss (%)</label>
            <input
              type="number"
              name="packet_loss"
              value={features.packet_loss}
              onChange={handleChange}
              min="0"
              max="100"
              step="0.01"
            />
          </div>
        </div>

        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? 'Detecting...' : 'Detect Anomaly'}
        </button>
      </form>

      {error && (
        <div className="error-message">
          <XCircle size={20} />
          <span>{error}</span>
        </div>
      )}

      {result && (
        <div className="result-card">
          <div className="result-header">
            <h3>Detection Result</h3>
            {result._demo && <span className="demo-badge">Demo Result</span>}
          </div>
          
          <div className="result-main">
            <div className={`status-badge ${result.is_anomaly ? 'anomaly' : 'normal'}`}>
              {result.is_anomaly ? <AlertTriangle size={32} /> : <CheckCircle size={32} />}
              <div>
                <div className="status-title">
                  {result.is_anomaly ? 'Anomaly Detected' : 'Normal Traffic'}
                </div>
                <div className="status-score">Score: {result.score.toFixed(3)}</div>
              </div>
            </div>
          </div>

          <div className="result-details">
            <div className="detail-item">
              <span className="label">Confidence</span>
              <span className="value">{(result.confidence * 100).toFixed(1)}%</span>
            </div>
            <div className="detail-item">
              <span className="label">Method</span>
              <span className="value">{result.method}</span>
            </div>
            <div className="detail-item">
              <span className="label">Isolation Forest Score</span>
              <span className="value">{result.methods.isolation_forest.score.toFixed(3)}</span>
            </div>
            <div className="detail-item">
              <span className="label">Autoencoder Score</span>
              <span className="value">{result.methods.autoencoder.score.toFixed(3)}</span>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default AnomalyDetection
