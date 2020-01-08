'''
Twitter APIを用いた処理は基本このプログラムで行う
'''
class TwitterInfo:
    def __init__(self, api):
        self.api = api
        self.getScreenName()

    # TwitterのID（固有識別子）を取得
    def getScreenName(self):
        self.screenName = self.api.VerifyCredentials().screen_name    
    def returnScreenName(self):
        return self.screenName

    '''
    リスト関連，ManageTabとUserTabで利用
    '''
    # 所持しているリスト一覧を取得
    def returnListNameList(self):
        listNameList = self.api.GetLists(screen_name=self.returnScreenName())
        listNameList = [l.name for l in listNameList]
        listNameList.append("Follow")
        return listNameList
    # 選択したリストのメンバー一覧を取得
    def returnListMember(self, listName):
        return [u.screen_name for u in self.api.GetListMembers(slug=listName, owner_screen_name=self.screenName)]
    def returnNumList(self):
        return self.api.GetLists(screen_name=self.screenName)
    # リストからユーザを除外
    def RemoveListUser(self, slug="", user=""):
        self.api.DestroyListsMember(slug=slug, owner_screen_name=self.screenName, screen_name=user)
    # リストにユーザを追加
    def AddListUser(self, slug="", user=""):
        self.api.CreateListsMember(slug=slug, owner_screen_name=self.screenName, screen_name=user)
    # どのリストにユーザが追加されているかをチェック
    def returnListMemberShip(self, selectUser):
        return self.api.GetMemberships(screen_name=selectUser, filter_to_owned_lists=True)

    # 選択したユーザの投稿した画像を抽出
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
    フォロー関連，ManageTabとUserTabで利用
    '''
    # フォローしているユーザの一覧を取得
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
        try:
            [followUsers.append(followUserList[j][2][i].screen_name) for j in range(len(followUserList)) for i in range(len(followUserList[j][2]))]
        except TypeError:
            pass
        self.followUsers = followUsers
        return followUsers
    # 選択したユーザのフォローを解除
    def RemoveFollowUser(self, user=""):
        self.api.DestroyFriendship(screen_name=user)
    # 選択したユーザをフォロー
    def AddFollowUser(self, user=""):
        self.api.CreateFriendship(screen_name=user, follow=False)