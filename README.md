# Notion Metrics Recorder

Notionデータベースのレコード数を定期的に記録し、Google Spreadsheetに保存するツールです。

## 機能

- 2つのNotionデータベースのレコード数を取得
- 取得したデータをGoogle Spreadsheetに記録
- 日時と各データベースのレコード数を自動的に記録
- macOSのLaunchAgentとして自動実行可能

## セットアップ

### 前提条件

- Python 3.8以上
- Notion APIキー
- Google Cloud Platformのプロジェクトと認証情報

### インストール

1. リポジトリをクローン
```bash
git clone https://github.com/yourusername/notion-metrics-recorder.git
cd notion-metrics-recorder
```

2. 仮想環境を作成してアクティベート
```bash
python3 -m venv venv
source venv/bin/activate  # Linuxの場合
# または
.\venv\Scripts\activate  # Windowsの場合
```

3. 必要なパッケージをインストール
```bash
pip install -r requirements.txt
```

### 設定

1. `.env.example`を`.env`にコピーして、必要な情報を設定
```bash
cp .env.example .env
```

2. `.env`ファイルに以下の情報を設定
- `NOTION_API_KEY`: NotionのAPIキー
- `NOTION_DATABASE_ID1`: 1つ目のNotionデータベースID
- `NOTION_DATABASE_ID2`: 2つ目のNotionデータベースID
- `GOOGLE_SPREADSHEET_ID`: 記録先のGoogle Spreadsheet ID
- `GOOGLE_SHEET_NAME`: 記録先のシート名

3. Google Cloud Platformで認証情報を設定
- Google Cloud Consoleでプロジェクトを作成
- Google Sheets APIを有効化
- OAuth 2.0クライアントIDを作成
- 認証情報をダウンロードして`credentials.json`として保存

## 使用方法

### 手動実行

```bash
python notion-metrics-recorder.py
```

初回実行時は、Google認証のためのブラウザが開きます。認証を完了すると、Notionのレコード数がGoogle Spreadsheetに記録されます。

### 自動実行（macOS）

1. スクリプトに実行権限を付与
```bash
chmod +x run.sh install.sh
```

2. LaunchAgentとしてインストール
```bash
./install.sh
```

これにより、システム起動時に自動的に実行され、1時間ごとにNotionのレコード数を記録します。

ログは以下の場所に出力されます：
- 標準出力: `~/Library/Logs/notion-metrics-recorder/stdout.log`
- エラー出力: `~/Library/Logs/notion-metrics-recorder/stderr.log`

## データ形式

Google Spreadsheetには以下の形式でデータが記録されます：

- A列: 日時（YYYY-MM-DD HH:MM:SS）
- B列: データベース1のレコード数
- C列: データベース2のレコード数

## 注意事項

- `.env`ファイルと`credentials.json`はGitにコミットしないでください
- 認証情報は適切に管理してください
- 初回実行時のみGoogle認証が必要です
- 自動実行時は、初回のGoogle認証を手動で行う必要があります

## ライセンス

MIT License