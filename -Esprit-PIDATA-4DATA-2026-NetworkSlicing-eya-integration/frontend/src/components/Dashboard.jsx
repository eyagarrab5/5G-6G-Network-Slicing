import React, { useState, useEffect } from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, BarChart, Bar } from 'recharts'
import { Activity, Clock, AlertCircle, TrendingUp } from 'lucide-react'
import './Dashboard.css'

function Dashboard() {
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [metrics, setMetrics] = useState(null)

  useEffect(() => {
    fetchDashboardData()
  }, [])

  const fetchDashboardData = async () => {
    try {
      setLoading(true)
      const response = await fetch('/api/v1/dashboard/data')
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status_code}`)
      }
      
      const data = await response.json()
      setMetrics(data)
    } catch (err) {
      console.error('Failed to fetch dashboard data:', err)
      setError('Unable to connect to backend services. Showing demo data.')
      setMetrics(getDemoData())
    } finally {
      setLoading(false)
    }
  }

  const getDemoData = () => ({
    slices: [
      { slice_id: 'demo_slice_001', qos_score: 0.85, congestion_level: 'Normal', slice_latency: 150, slice_transfer_rate: 8.5 },
      { slice_id: 'demo_slice_002', qos_score: 0.72, congestion_level: 'Light', slice_latency: 280, slice_transfer_rate: 6.2 },
      { slice_id: 'demo_slice_003', qos_score: 0.45, congestion_level: 'Critical', slice_latency: 450, slice_transfer_rate: 3.1 },
    ],
    alerts: [
      { id: 1, level: 'CRITICAL', message: 'Demo: Critical congestion detected', acknowledged: false },
      { id: 2, level: 'WARN', message: 'Demo: High latency warning', acknowledged: false },
    ],
    timestamp: new Date().toISOString()
  })

  const latencyData = metrics?.slices?.map(slice => ({
    name: slice.slice_id,
    latency: slice.slice_latency || 0
  })) || []

  const throughputData = metrics?.slices?.map(slice => ({
    name: slice.slice_id,
    throughput: slice.slice_transfer_rate || 0
  })) || []

  const packetLossData = metrics?.slices?.map(slice => ({
    name: slice.slice_id,
    packetLoss: slice.slice_packet_loss || 0
  })) || []

  if (loading) {
    return (
      <div className="dashboard loading">
        <div className="spinner"></div>
        <p>Loading dashboard data...</p>
      </div>
    )
  }

  return (
    <div className="dashboard">
      {error && (
        <div className="error-banner">
          <AlertCircle size={20} />
          <span>{error}</span>
        </div>
      )}

      <div className="metrics-grid">
        <div className="metric-card">
          <div className="metric-icon latency">
            <Clock size={24} />
          </div>
          <div className="metric-content">
            <h3>Average Latency</h3>
            <p className="metric-value">
              {metrics?.slices?.length > 0 
                ? `${Math.round(metrics.slices.reduce((acc, s) => acc + (s.slice_latency || 0), 0) / metrics.slices.length)} μs`
                : 'N/A'}
            </p>
            <span className="metric-label">Demo Data</span>
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-icon throughput">
            <TrendingUp size={24} />
          </div>
          <div className="metric-content">
            <h3>Average Throughput</h3>
            <p className="metric-value">
              {metrics?.slices?.length > 0
                ? `${(metrics.slices.reduce((acc, s) => acc + (s.slice_transfer_rate || 0), 0) / metrics.slices.length).toFixed(2)} Gbps`
                : 'N/A'}
            </p>
            <span className="metric-label">Demo Data</span>
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-icon packet-loss">
            <Activity size={24} />
          </div>
          <div className="metric-content">
            <h3>Packet Loss Rate</h3>
            <p className="metric-value">
              {metrics?.slices?.length > 0
                ? `${(metrics.slices.reduce((acc, s) => acc + (s.slice_packet_loss || 0), 0) / metrics.slices.length * 100).toFixed(3)}%`
                : 'N/A'}
            </p>
            <span className="metric-label">Demo Data</span>
          </div>
        </div>

        <div className="metric-card">
          <div className="metric-icon alerts">
            <AlertCircle size={24} />
          </div>
          <div className="metric-content">
            <h3>Active Alerts</h3>
            <p className="metric-value">{metrics?.alerts?.length || 0}</p>
            <span className="metric-label">Demo Data</span>
          </div>
        </div>
      </div>

      <div className="charts-grid">
        <div className="chart-card">
          <h3>Latency by Slice (Demo Data)</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={latencyData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="latency" fill="#3b82f6" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h3>Throughput by Slice (Demo Data)</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={throughputData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="throughput" stroke="#22c55e" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h3>Packet Loss by Slice (Demo Data)</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={packetLossData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="packetLoss" fill="#ef4444" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {metrics?.alerts?.length > 0 && (
        <div className="alerts-section">
          <h3>Recent Alerts (Demo Data)</h3>
          <div className="alerts-list">
            {metrics.alerts.map(alert => (
              <div key={alert.id} className={`alert-item ${alert.level.toLowerCase()}`}>
                <AlertCircle size={20} />
                <span>{alert.message}</span>
                <span className={`alert-badge ${alert.level.toLowerCase()}`}>{alert.level}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default Dashboard
