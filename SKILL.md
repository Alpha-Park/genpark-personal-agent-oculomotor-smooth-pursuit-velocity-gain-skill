---
name: genpark-personal-agent-oculomotor-smooth-pursuit-velocity-gain-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating oculomotor smooth pursuit velocity gain, retinal velocity error, and saccadic substitution kinetics.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Oculomotor Smooth Pursuit Tracking Skill

A sovereign personal agent capability for evaluating continuous visual pursuit gain, cerebellar-frontal oculomotor control, and quantifying saccadic substitution during dynamic visual tracking.

## Core Capabilities
- **Smooth Pursuit Velocity Gain**: Compares slow-phase continuous eye tracking speed to target velocity.
- **Saccadic Substitution Audit**: Detects choppy visual catch-up saccades that replace continuous smooth pursuit.
- **Phase Lag Tracking**: Quantifies the temporal latency between target movement and compensatory eye motion.
- **Visual Ergonomics**: Actionable figure-8 convergence exercises and screen refresh optimizations.

## Fast Invocation
```python
from client import OculomotorSmoothPursuitClient

client = OculomotorSmoothPursuitClient()
res = client.evaluate_smooth_pursuit(
    target_velocity_deg_s=20.0,
    eye_smooth_velocity_deg_s=19.4,
    catchup_saccade_frequency_hz=0.4
)
print("Pursuit Gain:", res["smooth_pursuit_gain"])
print("Tracking Score:", res["oculomotor_tracking_score"])
```
