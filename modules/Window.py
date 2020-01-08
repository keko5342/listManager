'''
全体の基礎となるウインドウを管理，各種タブの画面配置を行う
'''
import MonitorInfo
import UserTab, IllustTab, ManageTab
from tkinter import *

class Window:
    def __init__(self, monitorInfo, api):
        # ディスプレイの情報を取得
        self.monitorInfo = monitorInfo
        self.monitorHeight = self.monitorInfo.returnMonitorHeight()
        self.monitorWidthHarfed = self.monitorInfo.returnMonitorWidth(2)
        self.monitorWidthQuoted = self.monitorInfo.returnMonitorWidth(4)
        self.setup()

        # Tabをウインドウに配置
        self.userTab = UserTab.UserTab(master=self.root, width=self.monitorWidthQuoted, height=self.monitorHeight, api=api)
        self.userTab.scrollListBox.bind("<Button-1>", self.scrollListClickedEvent)
        self.illustTab = IllustTab.IllustTab(master=self.root, width=self.monitorWidthHarfed, height=self.monitorHeight, api=api)
        self.manageTab = ManageTab.ManageTab(master=self.root, width=self.monitorWidthQuoted, height=self.monitorHeight, api=api)
        [self.manageTab.checkBoxList[i].bind("<Button-1>", self.checkBoxClickedEvent) for i in range(len(self.manageTab.checkBoxList))]

    # ウインドウの初期化
    def setup(self):
        root = Tk()
        root.option_add('*font', ('FixedSys', 14))
        root.title('listManager')
        root.geometry(self.monitorInfo.returnMonitorInfo()[0])
        root.state('zoomed')
        self.root = root
    # メインループの実行
    def excute(self):
        self.root.mainloop()
    def returnRoot(self, component):
        self.root = component.returnComponent(self.root)

    '''
    グローバルなイベント
    '''
    # UserTabでユーザが選択されたことをトリガーにManageTabでどのリストに入っているかを検索，IlustTabで投稿画像を抽出
    def scrollListClickedEvent(self, event):
        self.selectUser = self.userTab.returnSelectUser(event)
        print(self.selectUser)
        self.manageTab.listExistCheck(self.selectUser)
        self.manageTab.followExistCheck(self.selectUser)
        imageUrl = self.userTab.twitterInfo.getImageURL(self.selectUser)
        self.illustTab.downloadFourImage(imageUrl, self.monitorWidthQuoted)
    # ManageTabでのリストへの追加削除の操作をトリガーにリクエストを送信
    def checkBoxClickedEvent(self, event):
        self.manageTab.checkBoxClicked(event, self.selectUser)