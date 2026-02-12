import json

print(json.dumps({
  "findings": [
    {
      "type": "policy_drift",
      "detail": "security-scan step removed from pipeline"
    }
  ]
}, indent=2))
