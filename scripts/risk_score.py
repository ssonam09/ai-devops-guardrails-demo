import json, sys

local = json.load(open(sys.argv[1]))
aml   = json.load(open(sys.argv[2]))

score = 0
reasons = []

if local.get("findings"):
    score += 40
    reasons.append("Local pipeline drift detected")

if aml.get("drift_alert") is True:
    score += 60
    reasons.append("Azure ML drift alert triggered")

decision = "auto-approve" if score < 50 else "needs-approval"

print(json.dumps({
  "risk_score": score,
  "decision": decision,
  "reasons": reasons
}, indent=2))

