from tkinter import *

class ManageTab(Frame):
    def __init__(self, master=None, width=0, height=0):
        super().__init__(master)
        self['bg'] = 'red'
        self['width'] = width
        self['height'] = height
        self.create_widgets()
        self.place(relx=0.75, rely=0.0)

    def create_widgets(self):
        widgetWidthMargin = 0.01
        widgetHeightMargin = 0.003

        self.manageTabLabel = Label(self, text='ManageTab').place(relwidth=0.33, relheight=0.025 - widgetHeightMargin * 2, relx=widgetWidthMargin, rely=widgetHeightMargin)

'''
lc = Label(frame3, text='リスト一覧', bg='yellow', relief=RIDGE, bd=2)
lc.place(relx=0.0, rely=0.0)
flgChkList = [BooleanVar() for i in range(len(lists))]
ChkBoxList = [Checkbutton(frame3, text=lists[n], variable=flgChkList[n]) for n in range(len(lists))]
for n in range(len(ChkBoxList)):
    flgChkList[n].set(False)
    ChkBoxList[n].bind("<Button-1>", chkBtnCallBack)
    ChkBoxList[n].place(relx=0.0, rely=(0.03 + 0.03 * n))
root.mainloop()
'''