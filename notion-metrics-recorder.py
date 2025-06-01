import requests

# 🛠️ あなたのNotion統合のシークレットキー
NOTION_API_KEY = "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"
# 🗂️ データベースID（URLから取得）
DATABASE_ID = "130a58238daa809884c0ed1d6338ca32"

def count_notion_records():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": "2022-06-28",  # 現時点の安定版
        "Content-Type": "application/json"
    }

    has_more = True
    next_cursor = None
    total_records = 0

    while has_more:
        body = {}
        if next_cursor:
            body["start_cursor"] = next_cursor

        response = requests.post(url, headers=headers, json=body)
        try:
            data = response.json()
        except Exception as e:
            print("❌ レスポンスの解析に失敗しました:", e)
            return

        if response.status_code != 200:
            print("❌ エラーが発生しました:", data)
            return

        results = data.get("results", [])
        total_records += len(results)
        has_more = data.get("has_more", False)
        next_cursor = data.get("next_cursor", None)

    print(f"✅ データベース内のレコード数: {total_records}")

if __name__ == "__main__":
    count_notion_records()