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

    def returnFollowUser(self):
        followUserList = []
        followUsers = []
        for j in range(15):
            if j == 0:
                followUserList.append(self.api.GetFriendsPaged(screen_name=self.screenName))
            else:
                followUserList.append(self.api.GetFriendsPaged(screen_name=self.screenName, cursor=followUserList[j - 1][0]))
            if followUserList[j][0] == 0:
                break
        print(followUserList)
        try:
            [followUsers.append(followUserList[j][2][i].screen_name) for j in range(len(followUserList)) for i in range(len(followUserList[j][2]))]
            return followUsers
        except TypeError:
            return followUsers

    def returnListMember(self, listName):
        return [u.screen_name for u in self.api.GetListMembers(slug=listName, owner_screen_name=self.screenName)]

    def getImageURL(self, selectUser):
        plainUrlList = self.api.GetUserTimeline(screen_name=selectUser, count=200, include_rts=False)
        urlList = []
        for i in range(len(plainUrlList)):
            try:
                urlList.append(plainUrlList[i].media[0].media_url)
            except TypeError:
                pass
        return urlList
        '''
        dld4Image()
        strExtImage = '追加読み込み(後' + str(len(urls)) + '枚)'
        nxtImgButton.configure(text=strExtImage)
        '''

    def __init__(self, api):
        self.api = api
        self.getScreenName()