import config
import sqlite3, urllib, webbrowser, twitter
from tkinter import *
import oauth2 as oauth
import tkinter.ttk as ttk

# Token
class AccessTokenCollector:
    # Request AccessToken at Local Database
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

    # Fetch New Twitter Access Token
    def fetchNewAccessToken(self):
        request_token_url = 'https://api.twitter.com/oauth/request_token'
        access_token_url = 'https://api.twitter.com/oauth/access_token'
        authorize_url = 'https://api.twitter.com/oauth/authorize'

        consumer = oauth.Consumer(self.CK, self.CS)
        client = oauth.Client(consumer)

        # Step 1: Get a request token. This is a temporary token that is used for
        # having the user authorize an access token and to sign the request to obtain
        # said access token.
        resp, content = client.request(request_token_url, "GET")
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])

        request_token = dict(urllib.parse.parse_qsl(content))

        # Step 2: Redirect to the provider. Since this is a CLI script we do not
        # redirect. In a web application you would redirect the user to the URL
        # below.
        url = "%s?oauth_token=%s" % (
            authorize_url, request_token[b'oauth_token'].decode())
        webbrowser.open(url)

        # After the user has granted access to you, the consumer, the provider will
        # redirect you to whatever URL you have told them to redirect to. You can
        # usually define this in the oauth_callback argument as well.
        oauth_verifier = self.getPIN()
        self.athRoot.destroy()

        # Step 3: Once the consumer has redirected the user back to the oauth_callback
        # URL you can request the access token the user has approved. You use the
        # request token to sign this request. After this is done you throw away the
        # request token and use the access token returned. You should store this
        # access token somewhere safe, like a database, for future use.
        token = oauth.Token(request_token[b'oauth_token'],
        request_token[b'oauth_token_secret'])
        token.set_verifier(oauth_verifier)
        client = oauth.Client(consumer, token)

        resp, content = client.request(access_token_url, "POST")
        access_token = dict(urllib.parse.parse_qsl(content))

        #access_tokenをデータベースに保存
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

    def getPIN(self):
        athLabel = Label(self.athRoot, text="認証画面で出るPINを入力してね").pack()
        athEntry = Entry(self.athRoot)
        athEntry.pack()
        athLabel2 = Label(self.athRoot, text="モニタ解像度").pack()
        athCombo = ttk.Combobox(self.athRoot, state='readonly')
        athCombo["values"] = self.monitorInfo
        athCombo.current(0)
        athCombo.pack()
        athSubmit = Button(self.athRoot, text="決定", command=self.smtClicked).pack()
        self.athRoot.mainloop()

        return athEntry.get()

    def smtClicked(self):
        self.athRoot.quit()

    def showVariables(self):
        print("AT={0}, ATS={1}, CK={2}, CS={3}".format(self.AT, self.ATS, self.CK, self.CS))

    def returnApi(self):
        return self.api

    def __init__(self, monitorInfo):
        self.monitorInfo = monitorInfo
        self.AT = ""
        self.ATS = ""
        self.CK = config.CONSUMER_KEY
        self.CS = config.CONSUMER_SECRET
        self.getAccessToken()
        self.api = twitter.Api(self.CK, self.CS, self.AT, self.ATS)
        #self.scrName = self.api.VerifyCredentials().screen_name
        #self.listNames = [l.name for l in self.api.GetLists(screen_name=self.scrName)].append("Follow")