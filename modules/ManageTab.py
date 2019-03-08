import TwitterInfo
from tkinter import *

class ManageTab(Frame):
    def __init__(self, master=None, width=0, height=0, api=0):
        # Get TwitterInfo
        self.twitterInfo = TwitterInfo.TwitterInfo(api)

        # Frame Initalize
        super().__init__(master)
        self['bg'] = 'red'
        self['width'] = width
        self['height'] = height
        self.create_widgets()

        # Bounding Frame
        self.place(relx=0.75, rely=0.0, relwidth=0.25, relheight=1.0)
    
    def checkBoxClicked(self, event, user):
        try:
            checkBoxNum = int(str(event.widget)[24:]) - 1
            if self.checkBoxFlags[checkBoxNum] == False:
                if len(self.checkBoxFlags) == checkBoxNum:
                    self.twitterInfo.RemoveFollowUser(user=user)
                else:
                    listName = self.checkBoxList[checkBoxNum].cget("text")
                    self.twitterInfo.RemoveListUser(slug=listName, user=user)
            else:
                if len(self.checkBoxFlags) == checkBoxNum:
                    self.twitterInfo.AddFollowUser(user=user)
                else:
                    listName = self.checkBoxList[checkBoxNum].cget("text")
                    self.twitterInfo.AddListUser(slug=listName, user=user)
        except ValueError:
            listName = self.checkBoxList[0].cget("text")
            if self.checkBoxFlags[0] == False:
                self.twitterInfo.RemoveListUser(slug=listName, user=user)
            else:
                self.twitterInfo.AddListUser(slug=listName, user=user)

    def listExistCheck(self, selectUser):
        listMemberShip = self.twitterInfo.returnListMemberShip(selectUser)
        listExist = []
        [listExist.append(listMemberShip[i].slug) for i in range(len(listMemberShip))]
        print(listExist)
        for i in range(len(self.checkBoxFlags)):
            self.checkBoxFlags[i].set(False)
            for j in range(len(listExist)):
                if self.checkBoxList[i].cget("text") == listExist[j]:
                    self.checkBoxFlags[i].set(True)

    def followExistCheck(self, selectUser):
        userList = self.twitterInfo.returnFollowUser()
        for i in range(len(userList)):
            if userList[i] == selectUser:
                self.checkBoxFlags[-1].set(True)
        '''                
            for i in range(len(ChkBoxList)):
                flgChkList[i].set(False)
                if i == (len(ChkBoxList) - 1):
                    print("lstFollower: " + str(lstFollower))
                    for j in range(len(lstFollower)):
                        if lstFollower[j] == selectUser:
                            print("Yes")
                            flgChkList[i].set(True)
        '''

    def create_widgets(self):
        widgetWidthMargin = 0.01
        widgetHeightMargin = 0.003

        self.manageTabLabel = Label(self, text='ManageTab').place(relwidth=0.33, relheight=0.025 - widgetHeightMargin * 2, relx=widgetWidthMargin, rely=widgetHeightMargin)
        ownerList = [i.name for i in self.twitterInfo.returnNumList()]
        self.checkBoxFlags = [BooleanVar() for i in range(len(ownerList) + 1)]
        [self.checkBoxFlags[i].set(False) for i in range(len(self.checkBoxFlags))]
        self.checkBoxList = [Checkbutton(self, text=ownerList[i], variable=self.checkBoxFlags[i]) for i in range(len(ownerList))]
        self.checkBoxList.append(Checkbutton(self, text="Follow", variable=len(self.checkBoxFlags)))
        [self.checkBoxList[i].place(relx=0.0, rely=(0.03 + 0.03 * i)) for i in range(len(self.checkBoxList))]