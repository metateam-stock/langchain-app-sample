# langchain-app-sample

Langchainを使用してOpenAI APIにリクエストを送り、結果を得るシンプルなPythonプログラム。

## 前提条件

- Python 3.x がインストールされていること
- Gitがインストールされていること
- OpenAI APIキーを取得していること

## セットアップ手順

### 1. リポジトリのクローン

まず、GitHubからこのリポジトリをクローンします。

```bash
git clone [リポジトリのURL]
cd [リポジトリ名]
```
### 2. 仮想環境の作成と有効化

プロジェクトのディレクトリ内で、Pythonの仮想環境を作成し、それを有効化します。  
Windowsの場合:
```bash
python -m venv venv
venv\Scripts\activate

```  
  
Linux/Macの場合:  
```bash
python -m venv venv
source venv/bin/activate

```  
  
### 3. 依存関係のインストール

`requirements.txt`` に記載されている依存パッケージをインストールします。  
```bash
pip install -r requirements.txt

```
  
### 4. 環境変数の設定
`.env` ファイルをプロジェクトディレクトリに作成し、OpenAI APIキーを設定します。
```plaintext
# .envファイル
OPENAI_API_KEY=あなたのAPIキー

```  
  
### 5. プログラムの実行
```bash
python main.py

```



