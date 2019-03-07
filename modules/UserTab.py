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
        self.place(relx=0.0, rely=0.0, relwidth=0.25, relheight=1.0)

    def create_widgets(self):
        widgetWidthMargin = 0.01
        widgetHeightMargin = 0.003

        self.topFrame = Frame(self, bg='purple')
        self.userTabLabel = Label(self.topFrame, text='UserTab').place(relwidth=0.33, relheight=0.5 - widgetHeightMargin * 2, relx=0.0, rely=0.0)
        self.listNameLabel = Label(self.topFrame, text='リスト名:').place(relwidth=0.2, relheight=0.5, relx=0.0, rely=0.5)
        self.listNameComboBox = ttk.Combobox(self.topFrame, state="readonly", values=self.twitterInfo.returnListNameList())
        self.listNameComboBox.current(0)
        self.listNameComboBox.place(relwidth=0.6, relheight=0.5, relx=0.2, rely=0.5)
        self.SubmitButton = Button(self.topFrame, text='設定', relief=RIDGE, command=self.setListMemberAtScrollList).place(relwidth=0.2, relheight=0.5, relx=0.8, rely=0.5)

        self.scrollListBox = Listbox(self)
        self.topFrame.place(relwidth=1.0 - widgetWidthMargin * 2, relheight=0.05 - widgetHeightMargin * 2,  \
            relx=widgetWidthMargin, rely=widgetHeightMargin)
        self.scrollListBox.place(relwidth=1.0 - widgetWidthMargin * 2, relheight=0.95 - widgetHeightMargin, \
            relx=widgetWidthMargin, rely=0.05)
    
    #setScrollList
    def setListMemberAtScrollList(self):
        # Clear Old List
        self.scrollListBox.delete(0, self.scrollListBox.size())

        # Fetch UserList
        screenName = self.twitterInfo.returnScreenName()
        if(self.listNameComboBox.get() == "Follow"):
            userList = self.twitterInfo.returnFollowUser()
        else:
            userList = self.twitterInfo.returnListMember(self.listNameComboBox.get())

        # Set List
        self.scrollListBox.insert(END, *userList) 

    def returnSelectUser(self, event):
        return self.scrollListBox.get(self.scrollListBox.nearest(event.y))