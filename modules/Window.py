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
    
    def __init__(self, monitorInfo, api):
        self.monitorInfo = monitorInfo
        monitorHeight = self.monitorInfo.returnMonitorHeight()
        monitorWidthHarfed = self.monitorInfo.returnMonitorWidth(2)
        monitorWidthQuoted = self.monitorInfo.returnMonitorWidth(4)
        self.setup()
        self.userTab = UserTab.UserTab(master=self.root, width=monitorWidthQuoted, height=monitorHeight, api=api)
        self.illustTab = IllustTab.IllustTab(master=self.root, width=monitorWidthHarfed, height=monitorHeight)
        self.manageTab = ManageTab.ManageTab(master=self.root, width=monitorWidthQuoted, height=monitorHeight)