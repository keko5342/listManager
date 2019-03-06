import AccessTokenCollector, MonitorInfo, Window
from tkinter import *

class ListManager:
    def main(self):
        self.setupAccessTokenCollector()
        self.api = self.accessTokenCollector.returnApi()
        self.showWindow()
    
    # Setup Twitter Auth Info
    def setupAccessTokenCollector(self):
        self.accessTokenCollector = AccessTokenCollector.AccessTokenCollector(self.monitorInfo.returnMonitorInfo())
        #self.AccessTokenCollector.showVariables()

    # Main Window
    def showWindow(self):
        self.window = Window.Window(self.monitorInfo, self.api)
        self.window.excute()

    def __init__(self):
        self.monitorInfo = MonitorInfo.MonitorInfo()
        self.main()

if __name__ == "__main__":
    listManager = ListManager()


'''
#twitterAPI
passes = []

usrList = []
try:
    listmembers = api.GetListMembers(slug=lists[0], owner_screen_name=scrName)
    usrList = [u.screen_name for u in listmembers]
except twitter.error.TwitterError:
    pass

#frame
frame1 = Frame(root, width = dekWdhQuote, height = dekFulHeight, bg = 'blue')
frame2 = Frame(root, width = dekWdhHarf, height = dekFulHeight, bg = 'red')
frame3 = Frame(root, width = dekWdhQuote, height = dekFulHeight, bg = 'yellow')
frame1.place(relx=0.0, rely=0.0)
frame2.place(relx=0.25, rely=0.0)
frame3.place(relx=0.75, rely=0.0)

#users_tab
urls = []
sctUser = []
lstFollow = []
lstFollower = []
listString = StringVar()
la = Label(frame1, text='リストメンバー', bg='yellow', relief=RIDGE, bd=2)
la.place(relx=0.0, rely=0.0)
lstNmeLabel = Label(frame1, text='リスト名:')
lstNmeLabel.place(relx=0.0, rely=0.03)
lstName = StringVar()
lstNmeCmbBox = ttk.Combobox(frame1, textvariable=lstName, width=20, state="readonly")
lstNmeCmbBox["values"] = lists
lstNmeCmbBox.current(0)
lstNmeCmbBox.place(relx=0.2, rely=0.03)
lstNmeSubmit = Button(frame1, text='設定', command=setList)
lstNmeSubmit.place(relx=0.85, rely=0.025)
srlListBox = Listbox(frame1, width=47, height=39)
srlListBox.insert(END, *usrList)
srlListBox.bind("<Button-1>", callback)
srlListBox.place(relx=0.0, rely=0.06)

#images_tab
lb = Label(frame2, text='画像', bg='yellow', relief=RIDGE, bd=2)
lb.place(relx=0.0, rely=0.0)
strExtImage = '追加読み込み(後' + str(len(urls)) + '枚)'
nxtImgButton = Button(frame2, text=strExtImage, command=nxtImage)
nxtImgButton.place(relx=0.1, rely=0.0)
grdFrame = Frame(frame2, width = dekWdhHarf, height = dekFulHeight, bg = 'white')
grdFrame.place(relx=0.0, rely=0.03)
lstLabel = setImage()

#lists_tab
lc = Label(frame3, text='リスト一覧', bg='yellow', relief=RIDGE, bd=2)
lc.place(relx=0.0, rely=0.0)
flgChkList = [BooleanVar() for i in range(len(lists))]
ChkBoxList = [Checkbutton(frame3, text=lists[n], variable=flgChkList[n]) for n in range(len(lists))]
for n in range(len(ChkBoxList)):
    flgChkList[n].set(False)
    ChkBoxList[n].bind("<Button-1>", chkBtnCallBack)
    ChkBoxList[n].place(relx=0.0, rely=(0.03 + 0.03 * n))
root.mainloop()
'''