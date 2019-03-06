import TwitterInfo
from tkinter import *

class UserTab(Frame):
    def __init__(self, master=None, width=0, height=0, api=0):
        # Get TwitterInfo
        self.twitterInfo = TwitterInfo.TwitterInfo(api)

        # Frame Initalize
        super().__init__(master)
        self['bg'] = 'blue'
        self['width'] = width
        self['height'] = height
        self.create_widgets()

        # Bounding Frame
        self.place(relx=0.0, rely=0.0)

    def create_widgets(self):
        widgetWidthMargin = 0.01
        widgetHeightMargin = 0.003

        self.topFrame = Frame(self, bg='purple')
        self.userTabLabel = Label(self.topFrame, text='UserTab').place(relwidth=0.33, relheight=0.5 - widgetHeightMargin * 2, relx=0.0, rely=0.0)
        self.listNameLabel = Label(self.topFrame, text='リスト名:').place(relwidth=0.2, relheight=0.5, relx=0.0, rely=0.5)
        self.listNameComboBox = ttk.Combobox(self.topFrame, state="readonly", values=self.twitterInfo.returnListNameList())
        self.listNameComboBox.current(0)
        self.listNameComboBox.place(relwidth=0.6, relheight=0.5, relx=0.2, rely=0.5)
        self.SubmitButton = Button(self.topFrame, text='設定', relief=RIDGE, command=self.setList).place(relwidth=0.2, relheight=0.5, relx=0.8, rely=0.5)

        self.scrollListBox = Listbox(self)
        self.topFrame.place(relwidth=1.0 - widgetWidthMargin * 2, relheight=0.05 - widgetHeightMargin * 2,  \
            relx=widgetWidthMargin, rely=widgetHeightMargin)
        self.scrollListBox.place(relwidth=1.0 - widgetWidthMargin * 2, relheight=0.95 - widgetHeightMargin, \
            relx=widgetWidthMargin, rely=0.05)
    
    #setScrollList
    def setList(self):
        self.scrollListBox.delete(0, self.scrollListBox.size())
        screenName = self.twitterInfo.returnScreenName()

        

        if self.listNameComboBox.get() == "Follow":
            for j in range(15):
                if j == 0:
                    followUserList.append(self.api.GetFriendsPaged(screen_name=screenName))
                else:
                    followUserList.append(self.api.GetFriendsPaged(screen_name=screenName, cursor=followUserList[j - 1][0]))
                if followUserList[j][0] == 0:
                    break
            for j in range(len(followUserList)):
                for i in range(len(followUserList[j][2])):
                    try:
                        followUsers.append(followUsers[j][2][i].screen_name)
                    except TypeError:
                        pass
            scrollListBox.insert(END, *followIsers)
            return
        self.listMember = self.api.GetListMembers(slug=listNameComboBox.get(), owner_screen_name=screenName)
        userList = [u.screen_name for u in listMember]
        self.scrollListBox.insert(END, *userList)

'''
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
'''