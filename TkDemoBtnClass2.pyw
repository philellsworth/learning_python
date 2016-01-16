from tkinter   import * ## For Button, pack(), mainloop()
from RandColor import * ## For random_color(), contrasting_color()

def getnext(pIdx,pLen):
    if (pIdx >= pLen):
        return -1
    if (pIdx == (pLen -1)):
        return 0
    else:
        return pIdx + 1

class cQuitBtn (Button):
    def __init__( self , parent=None , cnf={} ,**kw ):
        Button.__init__(self , parent , cnf , **kw )
        self['command']=self.Callback
        self.pack(fill=BOTH,expand=YES)
        print(type(self).__name__, ': Initialized',sep='')
    def Callback(self): # define a block of code to be executed when button clicked
        print(type(self).__name__, ': CallBack',sep="")
        gRoot.destroy()
    
class cClrBtn (Button):
    def __init__( self , parent=None , cnf={} ,**kw ):
        Button.__init__(self , parent , cnf , **kw )
        self['command']=self.Callback
        self.pack(fill=BOTH,expand=YES)
        self.TextColor=random_color()
        self.SetColor(self.TextColor)
        self.bind("<Button-3>",self.ManageRightClick)
        print(type(self).__name__, ': Initialized: TextColor(' , self.TextColor , ')', sep="")
    def SetColor(self,clr=None):
        if (clr==None):
            tmpBG = random_color()
            while (tmpBG == self.TextColor): 
                tmpBG = random_color()
            self.TextColor = tmpBG
        else:
            self.TextColor = clr
        self['fg']= self.TextColor
        self['bg']= contrasting_color(self.TextColor)
    def Callback(self): # define a block of code to be executed when button clicked
        iCurr = self.Idx
        iChangee = getnext (iCurr,len(self.OtherClrBtnList))
        while (iChangee != self.Idx):
            self.OtherClrBtnList[iChangee].SetColor(self.OtherClrBtnList[iCurr].TextColor) 
            iCurr=getnext(iCurr,len(self.OtherClrBtnList))
            iChangee=getnext(iCurr,len(self.OtherClrBtnList))
        self.SetColor()
        print(type(self).__name__, ': Called: TextColor(' , self.TextColor , ')' ,sep="")
    def ManageRightClick(self,event):
        self.SetColor()
        
gRoot = Tk() # Make root a handle to the main container for widgets
TimesBold36 = font.Font(family='Times', size=36, weight='bold')
gQuitBtn = cQuitBtn( gRoot , text='Quit?'  , font=TimesBold36 )
NumClrBtns = 3
gBtnList=[]
for iBtnNum in range(NumClrBtns):
    tClrBtn = cClrBtn(gRoot , text='Color'+str(iBtnNum) , font=TimesBold36 )
    gBtnList.append(tClrBtn)
    tClrBtn.OtherClrBtnList=gBtnList
    tClrBtn.Idx = iBtnNum
    
gRoot.mainloop()
