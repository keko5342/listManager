'''
config.pyの内容をもとにTwitter APIへOauth認証を行う
'''
import config
import sqlite3, urllib, webbrowser, twitter
from tkinter import *
import oauth2 as oauth
import tkinter.ttk as ttk

class AccessTokenCollector:
    def __init__(self, monitorInfo):
        self.monitorInfo = monitorInfo
        self.AT = ""
        self.ATS = ""
        self.CK = config.CONSUMER_KEY
        self.CS = config.CONSUMER_SECRET
        self.getAccessToken()
        self.api = twitter.Api(self.CK, self.CS, self.AT, self.ATS)

    # 既存のログイン情報が保存されているかをチェック
    def getAccessToken(self):
        conn = sqlite3.connect('access_token.db')
        try:
            c = conn.cursor()
            for sqlResult in c.execute('select * from token'):
                pass
            self.AT = sqlResult[0].decode()
            self.ATS = sqlResult[1].decode()
            print("access_tokenある！")
        except sqlite3.OperationalError:
            self.athRoot = Tk()
            self.athRoot.geometry("200x200+500+200")
            access_token = self.fetchNewAccessToken()
            self.AT = access_token[b'oauth_token'].decode()
            self.ATS = access_token[b'oauth_token_secret'].decode()
            print("access_tokenない！")
        conn.close()

    # ログイン情報が見つからなかった場合，新規でOauth認証のためのトークンを取得する
    def fetchNewAccessToken(self):
        request_token_url = 'https://api.twitter.com/oauth/request_token'
        access_token_url = 'https://api.twitter.com/oauth/access_token'
        authorize_url = 'https://api.twitter.com/oauth/authorize'

        consumer = oauth.Consumer(self.CK, self.CS)
        client = oauth.Client(consumer)

        resp, content = client.request(request_token_url, "GET")
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])

        request_token = dict(urllib.parse.parse_qsl(content))

        url = "%s?oauth_token=%s" % (
            authorize_url, request_token[b'oauth_token'].decode())
        webbrowser.open(url)

        oauth_verifier = self.getPIN()
        self.athRoot.destroy()

        token = oauth.Token(request_token[b'oauth_token'],
        request_token[b'oauth_token_secret'])
        token.set_verifier(oauth_verifier)
        client = oauth.Client(consumer, token)

        resp, content = client.request(access_token_url, "POST")
        access_token = dict(urllib.parse.parse_qsl(content))

        # ログイン情報をデータベースに保存
        dbname = 'access_token.db'
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        create_table = '''create table token (access_token varchar(64), access_token_secret varchar(64))'''
        try:
            c.execute(create_table)
        except sqlite3.OperationalError:
            pass
        sql = 'insert into token (access_token, access_token_secret) values (?, ?)'
        token = (access_token[b'oauth_token'], access_token[b'oauth_token_secret'])
        c.execute(sql, token)
        conn.commit()
        conn.close()

        return access_token

    # 認証に必要なPINをGUIのフォームで入力する
    def getPIN(self):
        athLabel = Label(self.athRoot, text="認証画面で出るPINを入力してね").pack()
        athEntry = Entry(self.athRoot)
        athEntry.pack()
        athLabel2 = Label(self.athRoot, text="モニタ解像度").pack()
        athCombo = ttk.Combobox(self.athRoot, state='readonly')
        athCombo["values"] = self.monitorInfo
        athCombo.current(0)
        athCombo.pack()
        athSubmit = Button(self.athRoot, text="決定", command=self.submitClicked).pack()
        self.athRoot.mainloop()

        return athEntry.get()
    # GUIのフォームを閉じる
    def submitClicked(self):
        self.athRoot.quit()
    # Tokenが無事に取得できているかを確認（デバッグ用）
    def showVariables(self):
        print("AT={0}, ATS={1}, CK={2}, CS={3}".format(self.AT, self.ATS, self.CK, self.CS))
    # Tokenを使用して取得したApiへの認証情報をTwitterInfoへ
    def returnApi(self):
        return self.api