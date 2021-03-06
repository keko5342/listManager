'''
画面真ん中のコンポーネント，左側のタブであるUserTabで選択したユーザの画像を収集表示する
'''
from tkinter import *
import os, time, urllib
from PIL import Image, ImageTk

class IllustTab(Frame):
    def __init__(self, master=None, width=0, height=0, api=0):
        # Tabの初期化
        super().__init__(master)
        self['bg'] = 'yellow'
        self['width'] = width
        self['height'] = height
        self.create_widgets()

        # Tabの配置
        self.place(relx=0.25, rely=0.0, relwidth=0.5, relheight=1.0)

    # TabにWidgetを配置
    def create_widgets(self):
        widgetWidthMargin = 0.01
        widgetHeightMargin = 0.003

        self.illustTabLabel = Label(self, text='IllustTab').place(relwidth=0.2, relheight=0.025 - widgetHeightMargin * 2, relx=widgetWidthMargin, rely=widgetHeightMargin)
        self.nextImageButton = Button(self, text="追加読み込み", relief=RIDGE).place(relwidth=0.2, relheight=0.025 - widgetHeightMargin * 2, relx=0.8 - widgetWidthMargin, rely=widgetHeightMargin)
        self.gridFrame = Frame(self, bg = 'white')
        self.gridFrame.place(relwidth=1.0 - widgetWidthMargin * 2, relheight=0.975 - widgetHeightMargin * 2, relx=widgetWidthMargin, rely=0.025 + widgetHeightMargin)

    # 画像を4件だけ抽出
    def downloadFourImage(self, imageUrl, monitorWidthQuated):
        download_dir = 'tmp'
        sleep_time_sec = 0.1
        try:
            os.mkdir("tmp")
        except FileExistsError:
            pass
        self.photoList = []
        for i in range(len(imageUrl)):
            filename = os.path.basename(imageUrl[i])
            dst_path = os.path.join(download_dir, filename)
            time.sleep(sleep_time_sec)

            img = self.downloadImage(imageUrl[i], dst_path)
            img = Image.open(dst_path, 'r')
            img.thumbnail((self['width'] / 2, self['height'] / 2))
            if img.mode != "RGB":
                try:
                    img = img.convert("RGB")
                    print("RGB converted")
                except IOError:
                    print("Cannot converted")
            img.save(dst_path, 'JPEG', quality=100, optimize=True)
            self.photoList.append(ImageTk.PhotoImage(file=dst_path))
            self.imageLabelList = [Label(self.gridFrame, text=i, width=self['width'] / 2, height=self['height'] / 2, image=self.photoList[i]).grid(row=(int)(i / 2), column=(i % 2), padx=2, pady=2, sticky=NE)]
            #os.remove(dst_path)
            if i >= 3:
                break
        i = 0
        while i <= 3:
            try:
                imageUrl.pop(0)
            except IndexError:
                pass
            i += 1

    # 画像を全件抽出（未使用）
    def downloadImage(self, url, dst_path):
        try:
            data = urllib.request.urlopen(url).read()
            with open(dst_path, mode="wb") as f:
                f.write(data)
        except urllib.error.URLError as e:
            print(e)