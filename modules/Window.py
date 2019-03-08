import MonitorInfo
import UserTab, IllustTab, ManageTab
from tkinter import *

class Window:
    def setup(self):
        root = Tk()
        root.option_add('*font', ('FixedSys', 14))
        root.title('listManager')
        root.geometry(self.monitorInfo.returnMonitorInfo()[0])
        root.state('zoomed')

        self.root = root

    def excute(self):
        self.root.mainloop()

    def returnRoot(self, component):
        self.root = component.returnComponent(self.root)

    # ListBox is Selected
    def userClickedListBox(self, event):
        selectUser = self.userTab.scrollListBox.get(self.userTab.scrollListBox.nearest(event.y))
        print("User Clicked {}".format(selectUser))
        imageUrl = self.userTab.twitterInfo.getImageURL(selectUser)
        self.illustTab.downloadFourImage(imageUrl, self.monitorWidthQuoted)
        '''
        #if lstNmeCmbBox.get() != "Follow":
        chkLstMember(selectUser)
        getImgURL(selectUser)
        setImage()
        sctUser.clear()
        sctUser.append(selectUser)
        '''
    
    def __init__(self, monitorInfo, api):
        self.monitorInfo = monitorInfo
        self.monitorHeight = self.monitorInfo.returnMonitorHeight()
        self.monitorWidthHarfed = self.monitorInfo.returnMonitorWidth(2)
        self.monitorWidthQuoted = self.monitorInfo.returnMonitorWidth(4)
        self.setup()

        # Create Sub Window
        self.userTab = UserTab.UserTab(master=self.root, width=self.monitorWidthQuoted, height=self.monitorHeight, api=api)
        self.illustTab = IllustTab.IllustTab(master=self.root, width=self.monitorWidthHarfed, height=self.monitorHeight)
        self.manageTab = ManageTab.ManageTab(master=self.root, width=self.monitorWidthQuoted, height=self.monitorHeight)

        # Add Event
        self.userTab.scrollListBox.bind("<Button-1>", self.userClickedListBox)