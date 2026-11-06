import React, { useState, useEffect } from 'react'
import { Activity, AlertTriangle, Network, Zap } from 'lucide-react'
import Dashboard from './components/Dashboard'
import PredictionForm from './components/PredictionForm'
import AnomalyDetection from './components/AnomalyDetection'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState('dashboard')
  const [serviceStatus, setServiceStatus] = useState('checking')

  useEffect(() => {
    checkServiceStatus()
  }, [])

  const checkServiceStatus = async () => {
    try {
      const response = await fetch('http://localhost:8000/health')
      if (response.ok) {
        setServiceStatus('online')
      } else {
        setServiceStatus('offline')
      }
    } catch (error) {
      setServiceStatus('offline')
    }
  }

  return (
    <div className="app">
      <header className="header">
        <div className="header-content">
          <div className="logo">
            <Network className="logo-icon" size={32} />
            <h1>5G/6G Network Slicing</h1>
          </div>
          <div className={`service-status ${serviceStatus}`}>
            <div className={`status-dot ${serviceStatus}`} />
            <span>{serviceStatus === 'online' ? 'API Online' : serviceStatus === 'offline' ? 'API Offline' : 'Checking...'}</span>
          </div>
        </div>
      </header>

      <nav className="nav">
        <button
          className={`nav-item ${activeTab === 'dashboard' ? 'active' : ''}`}
          onClick={() => setActiveTab('dashboard')}
        >
          <Activity size={18} />
          Dashboard
        </button>
        <button
          className={`nav-item ${activeTab === 'prediction' ? 'active' : ''}`}
          onClick={() => setActiveTab('prediction')}
        >
          <Zap size={18} />
          Prediction
        </button>
        <button
          className={`nav-item ${activeTab === 'anomaly' ? 'active' : ''}`}
          onClick={() => setActiveTab('anomaly')}
        >
          <AlertTriangle size={18} />
          Anomaly Detection
        </button>
      </nav>

      <main className="main">
        {activeTab === 'dashboard' && <Dashboard />}
        {activeTab === 'prediction' && <PredictionForm />}
        {activeTab === 'anomaly' && <AnomalyDetection />}
      </main>

      <footer className="footer">
        <p>© 2026 Network Slicing Platform | Demo Data Clearly Labeled</p>
      </footer>
    </div>
  )
}

export default App
