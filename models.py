"""
Data models for Project Chimera's Heart with strict type validation
"""
from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, validator
import hashlib
import json

class TelemetryData(BaseModel):
    """Individual telemetry reading with validation"""
    timestamp: datetime = Field(default_factory=datetime.now)
    frustration_score: float = Field(..., ge=0.0, le=1.0)
    ram_load_percent: float = Field(..., ge=0.0, le=100.0)
    adversarial_flags: List[str] = Field(default_factory=list)
    cpu_utilization: float = Field(..., ge=0.0, le=100.0)
    response_latency_ms: float = Field(..., ge=0.0)
    error_count: int = Field(..., ge=0)
    
    @validator('frustration_score')
    def validate_frustration(cls, v):
        if v > 0.8:
            raise ValueError('Frustration score exceeds critical threshold