"""
Example Usage: Oculomotor Smooth Pursuit Tracking Dynamics.
Demonstrates calculation of visual pursuit gain and saccadic substitution analysis.
"""

from client import OculomotorSmoothPursuitClient


def main():
    client = OculomotorSmoothPursuitClient()
    print("=== Oculomotor Smooth Pursuit Tracking Demo ===")

    # Test Case 1: Healthy smooth visual pursuit (20 deg/s target)
    res1 = client.evaluate_smooth_pursuit(
        target_velocity_deg_s=20.0,
        eye_smooth_velocity_deg_s=19.4,
        catchup_saccade_frequency_hz=0.4,
        phase_lag_ms=28.0
    )
    print("\nTest Case 1: Healthy Smooth Pursuit Tracking")
    print(f"  Target Velocity: {res1['target_velocity_deg_s']} deg/s | Eye Velocity: {res1['eye_smooth_velocity_deg_s']} deg/s")
    print(f"  Pursuit Gain: {res1['smooth_pursuit_gain']}")
    print(f"  Catch-up Saccade Frequency: {res1['catchup_saccade_frequency_hz']} Hz | Phase Lag: {res1['phase_lag_ms']} ms")
    print(f"  Tracking Score: {res1['oculomotor_tracking_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Impaired pursuit with saccadic substitution / cognitive fatigue
    res2 = client.evaluate_smooth_pursuit(
        target_velocity_deg_s=25.0,
        eye_smooth_velocity_deg_s=16.0,
        catchup_saccade_frequency_hz=2.2,
        phase_lag_ms=85.0
    )
    print("\nTest Case 2: Saccadic Substitution Pattern")
    print(f"  Pursuit Gain: {res2['smooth_pursuit_gain']}")
    print(f"  Saccade Frequency: {res2['catchup_saccade_frequency_hz']} Hz | Lag: {res2['phase_lag_ms']} ms")
    print(f"  Tracking Score: {res2['oculomotor_tracking_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
