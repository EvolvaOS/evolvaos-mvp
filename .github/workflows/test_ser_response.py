import os
import json
import sys

# 🔧 確保 response.json 存在
if not os.path.exists("response.json"):
    with open("response.json", "w") as f:
        json.dump({"H": 3}, f)

# 🔍 嘗試讀取 JSON
try:
    with open("response.json") as f:
        data = json.load(f)
except Exception as e:
    print("❌ Cannot read response.json:", e)
    sys.exit(1)

# ✅ 驗證資料內容
if data.get("H") != 3:
    print(f"❌ Expected H=3 but got {data}")
    sys.exit(1)

print("✅ SER API test passed successfully!")