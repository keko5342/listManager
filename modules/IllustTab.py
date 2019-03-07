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