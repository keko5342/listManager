# listManager
自作ソフト「listEditor」の改修版です。pythonで書かれているため、パッケージが対応していればどの環境でも動作します。

# What is listManager?
listManagerでは、以下のことが可能です。

1. 

# Usage
本稿はWindows用です。他OSをお使いの場合は適宜OSに沿ったコマンドをご入力ください。pipにてパッケージを導入するため、仮想環境の構築工程が含まれていますが、必要のない場合は飛ばしていただいて構いません。
1. git clone でソースコードをダウンロード
2. クローンしたlistManagerのディレクトリに移動
3. py -m venv listManager_venv で仮想環境の作成
4. .\listManager_venv\Scripts\activate で仮想環境を有効化
5. pip install python-twitter, oauth2, urllib3, screeninfo, pillow で必要なパッケージをダウンロード
6. py listManager.py でlistManagerを起動

