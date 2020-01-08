'''
ユーザの使用しているディスプレイのサイズを取得・整形する
'''
from screeninfo import get_monitors

class MonitorInfo:
    def __init__(self):
        self.getMonitorInfo()

    # geometry型に整形（geometry型にするのはtkinterのウインドウサイズ指定の型が指定されているため）
    def getMonitorInfo(self):
        monitorGeometry = []
        monitorWidth = []
        monitorHeight = []
        # マルチディスプレイの場合を想定
        for m in get_monitors():
            monitorGeometry.append(str(m.width) + 'x' + str(m.height))
            monitorWidth.append(m.width)
            monitorHeight.append(m.height)
        self.monitorGeometry = monitorGeometry
        self.monitorWidth = monitorWidth
        self.monitorHeight = monitorHeight
    
    # Width x Height，Width，Heightで整形したサイズを返す
    def returnMonitorInfo(self):
        return self.monitorGeometry
    def returnMonitorWidth(self):
        return self.monitorWidth[0]
    def returnMonitorWidth(self, num):
        return self.monitorWidth[0] / num
    def returnMonitorHeight(self):
        return self.monitorHeight[0]