class TwitterInfo:
    def returnListNameList(self):
        listNameList = self.api.GetLists(screen_name=self.returnScreenName())
        listNameList = [l.name for l in listNameList]
        listNameList.append("Follow")
        return listNameList
    
    def getScreenName(self):
        self.screenName = self.api.VerifyCredentials().screen_name
    
    def returnScreenName(self):
        return self.screenName

    def __init__(self, api):
        self.api = api
        self.getScreenName()