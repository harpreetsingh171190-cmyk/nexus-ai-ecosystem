# ==============================================================================
# Module: Environmental Stream Analytics & Sensor Correlation
# Author: Harpreet Singh
# Description: Vectorized statistical calculation for multi-monitor environmental sensor telemetry.
# ==============================================================================

import pandas as pd
import numpy as np

class EnvironmentalTelemetryAnalyzer:
    @staticmethod
    def calculate_pollutant_mean(df: pd.DataFrame, pollutant: str) -> float:
        clean_series = df[pollutant].dropna()
        return float(np.mean(clean_series)) if len(clean_series) > 0 else 0.0

    @staticmethod
    def compute_complete_observations(df: pd.DataFrame) -> pd.DataFrame:
        complete = df.dropna(subset=['sulfate', 'nitrate'])
        return complete.groupby('ID').size().reset_index(name='nobs')

    @staticmethod
    def evaluate_correlations(df: pd.DataFrame, threshold: int = 50) -> list:
        correlations = []
        for monitor_id, group in df.groupby('ID'):
            clean = group.dropna(subset=['sulfate', 'nitrate'])
            if len(clean) >= threshold:
                corr = np.corrcoef(clean['sulfate'], clean['nitrate'])[0, 1]
                correlations.append(round(float(corr), 4))
        return correlations
