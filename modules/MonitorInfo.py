from screeninfo import get_monitors

# Collect Monitor Property
class MonitorInfo:
    # geometry型に整形
    def getMonitorInfo(self):
        monitorGeometry = []
        for m in get_monitors():
            m = str(m).replace('monitor(', '')
            m = str(m).replace(')', '')
            monitorGeometry.append(m)
        self.monitorGeometry = monitorGeometry
    
    def returnMonitorInfo(self):
        return self.monitorGeometry

    def returnMonitorWidth(self):
        return int(self.monitorGeometry[0][0:4])

    def returnMonitorWidth(self, num):
        return int(self.monitorGeometry[0][0:4]) / num

    def returnMonitorHeight(self):
        try:
            monitorHeight58 = int(self.monitorGeometry[0][5:8])
            monitorHeight59 = int(self.monitorGeometry[0][5:9])
        except ValueError:
            pass

        try:
            monitorHeight = max(monitorHeight58, monitorHeight59)
        except UnboundLocalError:
            monitorHeight = int(monitorHeight58)
        
        return monitorHeight
    
    def __init__(self):
        print(get_monitors())
        self.getMonitorInfo()
