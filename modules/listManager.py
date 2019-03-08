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