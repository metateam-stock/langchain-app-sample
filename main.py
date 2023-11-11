from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

# .envファイルから環境変数を読み込む
load_dotenv()

# ChatOpenAIの生成。初期化時に環境変数からAPIキーを読み込む
chat = ChatOpenAI()

# ユーザーからの質問を設定
messages = [
    SystemMessage(content="You're a helpful assistant."),
    HumanMessage(content="サッカーは何人でするスポーツですか？")
]

# Langchainを使用してOpenAI APIにリクエストを送信し、応答を取得
response = chat.invoke(messages)

# 応答の最後のメッセージを表示
print(response.content)
