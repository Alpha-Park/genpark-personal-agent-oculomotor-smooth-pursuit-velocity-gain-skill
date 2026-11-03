# Oculomotor Smooth Pursuit Tracking Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Oculomotor Smooth Pursuit gain, retinal velocity error, and saccadic substitution kinetics.

```mermaid
flowchart TD
    TargetStimulus["Dynamic Visual Target Trajectory (Deg/s)"] --> EyeTracker["High-Speed Video Oculography (VOG)"]
    EyeTracker --> PursuitExtract["Decomposition: Smooth Pursuit vs Catch-Up Saccades"]
    PursuitExtract --> GainCalc["Velocity Gain & Phase Lag Calculations"]
    GainCalc --> PrecisionScore["Oculomotor Tracking Precision Engine"]
    PrecisionScore --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Oculomotor Physiology Standards**: Implements clinical eye-tracking velocity gain and phase angle calculations.
- **Visual Fatigue & Attention Biomarker**: Quantifies cognitive decoupling and saccadic substitution.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import OculomotorSmoothPursuitClient

client = OculomotorSmoothPursuitClient()
result = client.evaluate_smooth_pursuit(
    target_velocity_deg_s=20.0,
    eye_smooth_velocity_deg_s=19.4
)
print("Pursuit Gain:", result["smooth_pursuit_gain"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
