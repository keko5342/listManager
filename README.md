# listManager
自作ソフト「listEditor」の改修版です。pythonで書かれているため、パッケージが対応していればどの環境でも動作します。

# What is listManager?
listManagerでは、以下のことが可能です。

1. 

# Environmnet
1. python - 3.7.1で動作確認
2. python-twitter - pip, Twitter APIへのリクエストに使用
3. oauth2 - pip, API利用のためのoauth認証に利用
4. urllib3 - pip, httpリクエストに利用
5. screeminfo - pip, ディスプレイ情報を取得するために利用
6. pillow - pip, tkinterでpngやjpgを扱うために利用

# Usage
本稿はWindows用です。他OSをお使いの場合は適宜OSに沿ったコマンドをご入力ください。pipにてパッケージを導入するため、仮想環境の構築工程が含まれていますが、必要のない場合は飛ばしていただいて構いません。
1. git clone でソースコードをダウンロード
2. cd listManager でクローンしたlistManagerのディレクトリに移動
3. py -m venv listManager_venv で仮想環境の作成
4. .\listManager_venv\Scripts\activate で仮想環境を有効化
5. pip install python-twitter, oauth2, urllib3, screeninfo, pillow で必要なパッケージをダウンロード
6. py listManager.py でlistManager を起動

## コピー用
```コピー用
git clone ********
cd listManager
py -m venv listManager_venv
.\listManager_venv\Scripts\activate
pip install python-twitter, oauth2, urllib3, screeninfo, pillow
py listManager.py
```
