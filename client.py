"""
Oculomotor Smooth Pursuit Tracking & Retinal Velocity Error Engine.
Provides deterministic, zero-dependency modeling of continuous visual pursuit gain (Eye Vel / Target Vel),
catch-up saccade frequency, phase lag kinetics, and cerebellar/frontal oculomotor tracking precision.
"""

from typing import Dict, Any, List, Optional


class OculomotorSmoothPursuitClient:
    """
    Deterministic client for evaluating Oculomotor Smooth Pursuit performance.
    Measures visual pursuit velocity gain, retinal slip error, and saccadic substitution
    to quantify dynamic visual acuity, reading stamina, and cognitive fatigue.
    """

    def __init__(self):
        pass

    def evaluate_smooth_pursuit(
        self,
        target_velocity_deg_s: float,
        eye_smooth_velocity_deg_s: float,
        catchup_saccade_frequency_hz: float = 0.5,
        phase_lag_ms: float = 30.0
    ) -> Dict[str, Any]:
        """
        Calculates pursuit gain = eye_smooth_velocity / target_velocity.
        Healthy adult normative gain at 15-30 deg/s: 0.88 - 1.05 with minimal catch-up saccades (< 1.5 Hz).
        """
        if target_velocity_deg_s <= 0 or eye_smooth_velocity_deg_s < 0:
            return {"error": "Target velocity must be positive and eye velocity non-negative"}

        gain = round(eye_smooth_velocity_deg_s / target_velocity_deg_s, 2)
        velocity_error = round(abs(target_velocity_deg_s - eye_smooth_velocity_deg_s), 1)

        # Oculomotor Tracking Precision Score (0 - 100):
        # Target gain 0.90 - 1.04 with low saccades and lag < 40 ms -> 90 - 100.
        score = 80.0
        if 0.90 <= gain <= 1.04:
            score += 15.0
        elif 0.82 <= gain < 0.90:
            score += 5.0
        elif gain < 0.70:
            score -= 30.0
        elif gain < 0.82:
            score -= 15.0

        if phase_lag_ms <= 40.0:
            score += 5.0
        elif phase_lag_ms > 70.0:
            score -= 15.0

        if catchup_saccade_frequency_hz > 1.8:
            score -= 20.0
        elif catchup_saccade_frequency_hz > 1.0:
            score -= 10.0

        tracking_score = round(min(100.0, max(5.0, score)), 1)

        if tracking_score >= 85.0:
            tier = "OPTIMAL_SMOOTH_PURSUIT_TRACKING"
            interp = f"Exceptional continuous visual pursuit (gain {gain}, lag {phase_lag_ms} ms); precise foveal retention on moving targets."
            guidance = "Superior dynamic visual tracking and reading fluency. Ideal state for rapid visual scanning and continuous focus."
        elif tracking_score >= 70.0:
            tier = "PRESERVED_OCULOMOTOR_FOLLOWING"
            interp = f"Normal smooth pursuit tracking (gain {gain}, saccade frequency {catchup_saccade_frequency_hz} Hz); standard visual-motor coordination."
            guidance = "Normal visual tracking. Take periodic 20-20-20 distance breaks during continuous screen reading."
        elif gain < 0.75 or catchup_saccade_frequency_hz > 1.5:
            tier = "IMPAIRED_PURSUIT_SACCADIC_SUBSTITUTION"
            interp = f"Depressed smooth pursuit gain ({gain} < 0.75) with high saccadic intrusion ({catchup_saccade_frequency_hz} Hz); choppy visual tracking."
            guidance = "Oculomotor fatigue or cerebellar/frontal attentional decoupling. Perform figure-8 gaze convergence exercises and rest eyes."
        else:
            tier = "MILD_RETINAL_SLIP_LAG"
            interp = f"Borderline pursuit velocity error ({velocity_error} deg/s, phase lag {phase_lag_ms} ms); mild dynamic tracking slip."
            guidance = "Mild visual tracking lag. Optimize ambient lighting and screen font scaling to reduce ocular strain."

        return {
            "target_velocity_deg_s": target_velocity_deg_s,
            "eye_smooth_velocity_deg_s": eye_smooth_velocity_deg_s,
            "smooth_pursuit_gain": gain,
            "velocity_error_deg_s": velocity_error,
            "catchup_saccade_frequency_hz": catchup_saccade_frequency_hz,
            "phase_lag_ms": phase_lag_ms,
            "oculomotor_tracking_score": tracking_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
