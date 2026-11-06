from app import db
from datetime import datetime
import json


class Anomaly(db.Model):
    """Anomaly detection model"""
    __tablename__ = 'anomalies'
    
    id = db.Column(db.Integer, primary_key=True)
    slice_id = db.Column(db.String(100), nullable=True, index=True)
    score = db.Column(db.Float, nullable=False)
    is_anomaly = db.Column(db.Boolean, nullable=False, default=False)
    method = db.Column(db.String(50), nullable=True)
    isolation_forest_score = db.Column(db.Float, nullable=True)
    autoencoder_score = db.Column(db.Float, nullable=True)
    features_json = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'slice_id': self.slice_id,
            'score': self.score,
            'is_anomaly': self.is_anomaly,
            'method': self.method,
            'isolation_forest_score': self.isolation_forest_score,
            'autoencoder_score': self.autoencoder_score,
            'features': json.loads(self.features_json) if self.features_json else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    def __repr__(self):
        return f'<Anomaly {self.id}: {self.slice_id} - {self.is_anomaly}>'
