# Pythonイメージの使用
FROM python:3.8-slim

# 必要なシステム依存関係のインストール
RUN apt-get update && apt-get install -y \
    python3-dev \
    libnacl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの設定
WORKDIR /bot

# discord.pyのインストール
RUN python3 -m pip install -U discord.py

# Botのコードをコピー
COPY . .

# Botを実行
CMD ["python", "./bot.py"]