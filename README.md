# Notion Metrics Recorder

複数のNotionデータベースのメトリクスをGoogle Spreadsheetに記録するPythonスクリプトです。

## 機能

- 最大5つのNotionデータベースのメトリクスを記録
- 未定義のデータベースは自動的にスキップ
- タイムスタンプ付きでGoogle Spreadsheetにデータを記録
- 詳細なログ記録によるエラーハンドリング
- 任意設定のデータベースに対応

## 前提条件

- Python 3.7以上
- Notion APIキー
- Google Cloudプロジェクト（Sheets API有効化済み）
- Google API認証情報

## インストール

1. リポジトリをクローン:
```bash
git clone https://github.com/yourusername/notion-metrics-recorder.git
cd notion-metrics-recorder
```

2. 仮想環境を作成してアクティベート:
```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

3. 依存パッケージをインストール:
```bash
pip install -r requirements.txt
```

## 設定

1. プロジェクトのルートディレクトリに`.env`ファイルを作成し、以下の変数を設定:
```env
# Notion API設定
NOTION_API_KEY=your_notion_api_key_here
NOTION_DATABASE_ID_1=your_first_database_id_here
NOTION_DATABASE_ID_2=your_second_database_id_here
NOTION_DATABASE_ID_3=your_third_database_id_here  # 任意
NOTION_DATABASE_ID_4=your_fourth_database_id_here  # 任意
NOTION_DATABASE_ID_5=your_fifth_database_id_here  # 任意

# Google Spreadsheet設定
GOOGLE_SPREADSHEET_ID=your_spreadsheet_id_here
GOOGLE_SHEET_NAME=notion-metrics-recorder

# Google APIファイルパス
GOOGLE_CREDENTIALS_FILE=credentials.json
GOOGLE_TOKEN_FILE=token.json
```

2. Google API認証情報の設定:
   - Google Cloud Consoleにアクセス
   - 新しいプロジェクトを作成
   - Google Sheets APIを有効化
   - 認証情報（OAuth 2.0クライアントID）を作成
   - 認証情報をダウンロードして`credentials.json`として保存

## 使用方法

スクリプトを実行:
```bash
python notion-metrics-recorder.py
```

スクリプトは以下の処理を行います:
1. 設定された各Notionデータベースのレコード数をカウント
2. 未定義のデータベースをスキップ
3. タイムスタンプと共にGoogle Spreadsheetに記録
4. すべてのアクティビティとエラーをログに記録

## 出力形式

Google Spreadsheetには以下の列が含まれます:
- タイムスタンプ
- データベース1のレコード数
- データベース2のレコード数
- データベース3のレコード数（未定義の場合は空欄）
- データベース4のレコード数（未定義の場合は空欄）
- データベース5のレコード数（未定義の場合は空欄）

## エラーハンドリング

- 未定義のデータベースはエラーを発生させずにスキップ
- APIエラーは詳細をログに記録
- 認証エラーは適切に処理
- すべてのエラーはログファイルに記録

## ログ記録

ログは以下のファイルに出力されます:
- `stdout.log`: 標準出力
- `stderr.log`: エラーメッセージ

## コントリビューション

1. リポジトリをフォーク
2. 機能ブランチを作成
3. 変更をコミット
4. ブランチにプッシュ
5. プルリクエストを作成

## ライセンス

このプロジェクトはMITライセンスの下で公開されています - 詳細はLICENSEファイルを参照してください。

## アーキテクチャ決定記録

このプロジェクトの設計決定の詳細については、[アーキテクチャ決定記録](docs/adr/)を参照してください。