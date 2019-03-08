from tkinter import *

class IllustTab(Frame):
    def __init__(self, master=None, width=0, height=0, api=0):
        super().__init__(master)
        self['bg'] = 'yellow'
        self['width'] = width
        self['height'] = height
        self.create_widgets()

        self.place(relx=0.25, rely=0.0, relwidth=0.5, relheight=1.0)

    def create_widgets(self):
        widgetWidthMargin = 0.01
        widgetHeightMargin = 0.003

        self.illustTabLabel = Label(self, text='IllustTab').place(relwidth=0.2, relheight=0.025 - widgetHeightMargin * 2, relx=widgetWidthMargin, rely=widgetHeightMargin)
        self.nextImageButton = Button(self, text="追加読み込み", relief=RIDGE).place(relwidth=0.2, relheight=0.025 - widgetHeightMargin * 2, relx=0.8 - widgetWidthMargin, rely=widgetHeightMargin)
        self.gridFrame = Frame(self, bg = 'white')
        self.gridFrame.place(relwidth=1.0 - widgetWidthMargin * 2, relheight=0.975 - widgetHeightMargin * 2, relx=widgetWidthMargin, rely=0.025 + widgetHeightMargin)

    #4件だけ保存#
    def downloadFourImage(self, imageUrl, monitorWidthQuated):
        download_dir = 'tmp'
        sleep_time_sec = 0.1
        try:
            os.mkdir("tmp")
        except FileExistsError:
            pass
        for i in range(len(imageUrl)):
            filename = os.path.basename(imageUrl[i])
            dst_path = os.path.join(download_dir, filename)
            time.sleep(sleep_time_sec)
            img = download_image(imageUrl[i], dst_path)
            img = Image.open(dst_path, 'r')
            img.thumbnail((monitorWidthQuated, monitorWidthQuated))
            if img.mode != "RGB":
                try:
                    img = img.convert("RGB")
                    print("RGB converted")
                except IOError:
                    print("Cannot converted")
            lstLabel = [Label(grdFrame, text=i, width=monitorWidthQuated, height=monitorWidthQuated, image=passes[i]).grid(row=(int)(i / 2), column=(i % 2), padx=2, pady=2, sticky=NE) for i in range(len(passes))]
            img.save(dst_path, 'JPEG', quality=100, optimize=True)
            passes.append(ImageTk.PhotoImage(file=dst_path))
            os.remove(dst_path)
            if i >= 3:
                break
        i = 0
        while i <= 3:
            try:
                urls.pop(0)
            except IndexError:
                pass
            i += 1