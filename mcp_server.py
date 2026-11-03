"""
MCP Server for Oculomotor Smooth Pursuit Tracking Skill.
Exposes JSON-RPC Model Context Protocol tools for assessing visual pursuit gain, catch-up saccades, and tracking accuracy.
"""

import sys
import json
from typing import Dict, Any
from client import OculomotorSmoothPursuitClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_smooth_pursuit",
                "description": "Calculates smooth pursuit velocity gain, velocity error, catch-up saccade frequency, and oculomotor tracking score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "target_velocity_deg_s": {
                            "type": "number",
                            "description": "Angular velocity of the moving visual stimulus in deg/s (e.g. 20.0 deg/s)."
                        },
                        "eye_smooth_velocity_deg_s": {
                            "type": "number",
                            "description": "Compensatory smooth pursuit eye velocity in deg/s (e.g. 19.2 deg/s)."
                        },
                        "catchup_saccade_frequency_hz": {
                            "type": "number",
                            "description": "Frequency of corrective catch-up saccades in Hz (e.g. 0.6 Hz).",
                            "default": 0.5
                        },
                        "phase_lag_ms": {
                            "type": "number",
                            "description": "Temporal tracking lag in milliseconds (e.g. 35.0 ms).",
                            "default": 30.0
                        }
                    },
                    "required": ["target_velocity_deg_s", "eye_smooth_velocity_deg_s"]
                }
            }
        ]
    }


def handle_request(client: OculomotorSmoothPursuitClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_smooth_pursuit":
            res = client.evaluate_smooth_pursuit(
                target_velocity_deg_s=float(args.get("target_velocity_deg_s", 20.0)),
                eye_smooth_velocity_deg_s=float(args.get("eye_smooth_velocity_deg_s", 19.0)),
                catchup_saccade_frequency_hz=float(args.get("catchup_saccade_frequency_hz", 0.5)),
                phase_lag_ms=float(args.get("phase_lag_ms", 30.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = OculomotorSmoothPursuitClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
