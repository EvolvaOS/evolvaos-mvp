// App.js
import React, { useState } from 'react';

function App() {
  const [data, setData] = useState(null);

  const fetchData = async () => {
    // 從 Phase 2 筆記中確認 SER API endpoint
    const SER_API_URL = "https://ser-mvp.replit.app/ser"; 

    try {
      const res = await fetch(SER_API_URL, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        // 使用文件 Phase 4 提供的範例資料
        body: JSON.stringify({"nodes":[{"energy":1},{"energy":2}],"prob":[0.5,0.5]})
      });

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      setData(await res.json());

    } catch (error) {
      console.error("Error fetching SER data:", error);
      setData({ error: error.message || "Failed to fetch SER data." });
    }
  };

  return (
    <div>
      <h1>EvolvaOS MVP Viewer</h1>
      <button onClick={fetchData}>Run SER</button>
      {/* 顯示結果，如果 data 存在 */}
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Click 'Run SER' to get data from SER Engine...</p>
      )}
    </div>
  );
}

export default App;