import React, { useState } from 'react'
import { Zap, CheckCircle, XCircle } from 'lucide-react'
import './PredictionForm.css'

function PredictionForm() {
  const [networkType, setNetworkType] = useState('6g')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const [formData, setFormData] = useState({
    slice_id: 'demo_slice_001',
    latency_budget: 200,
    slice_latency: 150,
    packet_loss_budget: 0.01,
    slice_packet_loss: 0.005,
    jitter_budget: 50,
    slice_jitter: 30,
    data_rate_budget: 5,
    slice_transfer_rate: 6,
  })

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const endpoint = networkType === '6g' 
        ? '/api/v1/predictions/qos/6g'
        : '/api/v1/predictions/qos/5g'
      
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      })

      if (!response.ok) {
        throw new Error(`HTTP ${response.status_code}`)
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      console.error('Prediction failed:', err)
      setError('Unable to connect to prediction service. Showing demo result.')
      setResult(getDemoResult())
    } finally {
      setLoading(false)
    }
  }

  const getDemoResult = () => ({
    slice_id: formData.slice_id,
    qos_score: 0.78,
    congestion_level: 'Normal',
    sla_respected: true,
    pipeline: networkType.toUpperCase(),
    _demo: true
  })

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: parseFloat(e.target.value)
    })
  }

  return (
    <div className="prediction-form">
      <div className="form-header">
        <Zap size={28} />
        <div>
          <h2>{networkType === '6g' ? '6G' : '5G'} QoS Prediction</h2>
          <p>Predict network slice quality of service (Demo Mode)</p>
        </div>
      </div>

      <div className="network-toggle">
        <button
          className={`toggle-btn ${networkType === '6g' ? 'active' : ''}`}
          onClick={() => setNetworkType('6g')}
        >
          6G Network
        </button>
        <button
          className={`toggle-btn ${networkType === '5g' ? 'active' : ''}`}
          onClick={() => setNetworkType('5g')}
        >
          5G Network
        </button>
      </div>

      <form onSubmit={handleSubmit} className="form">
        <div className="form-grid">
          <div className="form-group">
            <label>Slice ID</label>
            <input
              type="text"
              name="slice_id"
              value={formData.slice_id}
              onChange={(e) => setFormData({ ...formData, slice_id: e.target.value })}
              placeholder="Enter slice ID"
            />
          </div>

          <div className="form-group">
            <label>Latency Budget (μs)</label>
            <input
              type="number"
              name="latency_budget"
              value={formData.latency_budget}
              onChange={handleChange}
              min="0"
            />
          </div>

          <div className="form-group">
            <label>Actual Latency (μs)</label>
            <input
              type="number"
              name="slice_latency"
              value={formData.slice_latency}
              onChange={handleChange}
              min="0"
            />
          </div>

          <div className="form-group">
            <label>Packet Loss Budget</label>
            <input
              type="number"
              name="packet_loss_budget"
              value={formData.packet_loss_budget}
              onChange={handleChange}
              min="0"
              max="1"
              step="0.001"
            />
          </div>

          <div className="form-group">
            <label>Actual Packet Loss</label>
            <input
              type="number"
              name="slice_packet_loss"
              value={formData.slice_packet_loss}
              onChange={handleChange}
              min="0"
              max="1"
              step="0.001"
            />
          </div>

          <div className="form-group">
            <label>Jitter Budget (μs)</label>
            <input
              type="number"
              name="jitter_budget"
              value={formData.jitter_budget}
              onChange={handleChange}
              min="0"
            />
          </div>

          <div className="form-group">
            <label>Actual Jitter (μs)</label>
            <input
              type="number"
              name="slice_jitter"
              value={formData.slice_jitter}
              onChange={handleChange}
              min="0"
            />
          </div>

          <div className="form-group">
            <label>Data Rate Budget (Gbps)</label>
            <input
              type="number"
              name="data_rate_budget"
              value={formData.data_rate_budget}
              onChange={handleChange}
              min="0"
              step="0.1"
            />
          </div>

          <div className="form-group">
            <label>Actual Transfer Rate (Gbps)</label>
            <input
              type="number"
              name="slice_transfer_rate"
              value={formData.slice_transfer_rate}
              onChange={handleChange}
              min="0"
              step="0.1"
            />
          </div>
        </div>

        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? 'Predicting...' : 'Predict QoS'}
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
            <h3>Prediction Result</h3>
            {result._demo && <span className="demo-badge">Demo Result</span>}
          </div>
          <div className="result-grid">
            <div className="result-item">
              <span className="label">Slice ID</span>
              <span className="value">{result.slice_id}</span>
            </div>
            <div className="result-item">
              <span className="label">QoS Score</span>
              <span className="value">{(result.qos_score * 100).toFixed(1)}%</span>
            </div>
            <div className="result-item">
              <span className="label">Congestion Level</span>
              <span className={`value congestion-${result.congestion_level.toLowerCase()}`}>
                {result.congestion_level}
              </span>
            </div>
            <div className="result-item">
              <span className="label">SLA Respected</span>
              <span className={`value ${result.sla_respected ? 'success' : 'failure'}`}>
                {result.sla_respected ? <CheckCircle size={20} /> : <XCircle size={20} />}
                {result.sla_respected ? 'Yes' : 'No'}
              </span>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default PredictionForm
