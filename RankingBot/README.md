# RankingBotの使い方
## 環境
Python 3.7

## ライブラリ
- [slackBot](https://github.com/lins05/slackbot)
- requests

## 事前準備
あらかじめ、Botを追加するSlackチャンネルに`Hubot`を追加しておいてください。
- [Hubotの設定](https://qiita.com/ryofu/items/f1dadc2093b3017b5beb#hubot-integration%E3%81%AE%E8%A8%AD%E5%AE%9A)

Hubotが作成できたら、APIトークンをメモしておくこと。  
作成したHubotをBot投稿するチャンネルに追加する。
※ HubotではないSlackアプリでもOK、かつ自作アプリでもOKですが、その場合はSlackのAPIScopeにお気をつけください。

## 起動方法
1. RankingBotをクローン or zipダウンロード
2. pythonの環境変数にSlackのAPIトークンとBotを起動させるチャンネルIDを設定

APIトークンは 'API_TOKEN' で登録  
チャンネルIDは 'CHANNEL' で登録  

※ 環境変数にいれない場合は、bot起動時の引数にトークンとチャンネルIDを指定すること.環境変数の方がおすすめ。

参考：
- [Pythonの依存ライブラリをプロジェクトごとに管理し、別マシンでも一括インストールできるようにする方法](https://qiita.com/windows222/items/affbc6f5af033287312e)
- [SlackのチャンネルIDを確認する方法](https://auto-worker.com/blog/?p=132)

3. `python3 run.py`で起動  
※ 引数で起動する場合は、`python run.py [API_TOKEN] [CHANNEL]`

4. [mention.py](https://github.com/TDroider/SlackBot/blob/master/RankingBot/plugins/mention.py)にある言葉をSlackで発言すればOK
