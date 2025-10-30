import json
import sys

try:
    with open("response.json") as f:
        data = json.load(f)
except Exception as e:
    print("❌ Cannot read response.json:", e)
    sys.exit(1)

if data.get("H") != 3:
    print(f"❌ Expected H=3 but got {data}")
    sys.exit(1)

print("✅ SER API test passed successfully!")