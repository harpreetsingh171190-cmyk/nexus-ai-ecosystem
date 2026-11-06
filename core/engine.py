# ==============================================================================
# Module: Nexus Core Security & Correlation Engine
# Author: Harpreet Singh
# Description: High-throughput log ingestion, rule-based correlation, and anomaly detection.
# ==============================================================================

import time
import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class SecurityLogEvent:
    source_ip: str
    destination_ip: str
    event_type: str
    severity_level: int
    timestamp: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)

class CorrelationRule:
    def __init__(self, rule_id: int, name: str, threshold: int, timeframe_sec: int, alert_level: int):
        self.rule_id = rule_id
        self.name = name
        self.threshold = threshold
        self.timeframe_sec = timeframe_sec
        self.alert_level = alert_level
        self.matched_events: List[SecurityLogEvent] = []

    def evaluate(self, event: SecurityLogEvent) -> Optional[Dict[str, Any]]:
        current_time = time.time()
        self.matched_events = [e for e in self.matched_events if current_time - e.timestamp <= self.timeframe_sec]
        self.matched_events.append(event)
        
        if len(self.matched_events) >= self.threshold:
            alert = {
                "rule_id": self.rule_id,
                "rule_name": self.name,
                "alert_level": self.alert_level,
                "triggered_at": current_time,
                "sample_event": event.__dict__,
                "count": len(self.matched_events)
            }
            self.matched_events = []
            return alert
        return None

class NexusCorrelationEngine:
    def __init__(self):
        self.rules: List[CorrelationRule] = [
            CorrelationRule(101, "Rapid Auth Failure (Brute Force)", threshold=5, timeframe_sec=30, alert_level=4),
            CorrelationRule(102, "Excessive Telemetry Anomaly", threshold=3, timeframe_sec=15, alert_level=3),
            CorrelationRule(103, "Agent API Rate Limit Breach", threshold=10, timeframe_sec=60, alert_level=2),
        ]
        self.alerts_history: List[Dict[str, Any]] = []

    def ingest_event(self, event: SecurityLogEvent) -> List[Dict[str, Any]]:
        alerts = []
        for rule in self.rules:
            result = rule.evaluate(event)
            if result:
                alerts.append(result)
                self.alerts_history.append(result)
        return alerts

if __name__ == "__main__":
    engine = NexusCorrelationEngine()
    print("[*] Ingesting test security log events...")
    for i in range(6):
        evt = SecurityLogEvent(
            source_ip="192.168.1.105",
            destination_ip="10.0.0.1",
            event_type="AUTH_FAILURE",
            severity_level=3
        )
        alerts = engine.ingest_event(evt)
        if alerts:
            print(f"[!] Alert Triggered: {alerts}")
