# Noko_bot
我が家の便利ChatGPT botです。<br>
親の「サイトにアクセスするのがだるい」という一声で制作を決意、ワイの財布から10ドル（1500円が消えました）<br>
なぜかチャージして使わなかったapi代、役に立って良かったね

# 環境
- Ubuntu 22.04 LTS（大学Server）
- Docker

# 作業ログなどについて
[ここから読めます](https://qiita.com/Kento210/items/3e2dc0d19e293c0202cc)

# 起動/停止
起動：`docker-compose start` <br>
停止：`docker-compose stop` or control + c

# 初回起動について
1. Dockerfileのあるディレクトリにて、`docker-compose build`を実行する
1. .envに`DISCORD_TOKEN`と`OPENAI_API_KEY`の項目を追加する
1. `docker-compose up`で起動

# bot.pyの更新時
一度コンテナを停止、書き換え後にもう一度起動してください

# Dockerfileの更新時
一度コンテナを停止、書き換え後に再度buildしてから起動してください