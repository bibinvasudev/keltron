import wx
import random



class alert(wx.Dialog):
    def __init__(self, parent, id, title,error):
	self.error = error
        wx.Dialog.__init__(self, parent, id, title, size=(300, 100))
	res=self.SetBackgroundColour(wx.Colour(31,123,15))
	
        font1 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'UnDotum')
	
	if self.error ==1:
        
		self.label = wx.StaticText(self, -1, '                                                                                                                                                                                                                                                             Cannot Connect      !!!!!!!!!!!!!!!!!!!!!                    Please check IP Address or Port number',(40,50))
	
	
	elif self.error ==2:

		self.label = wx.StaticText(self, -1,'Error in Connection !!!!!',(40,50))
	elif self.error ==3:
		self.label = wx.StaticText(self, 1,'                                                                                                CONNECTED !!!!!',pos =(70,50))

	elif self.error ==10:
		self.label = wx.StaticText(self, -1,'ENTER TIME INTERVEL !!!!!',(40,50))
	elif self.error ==11:
		self.label = wx.StaticText(self, -1,'ENYER PORT NUMBER !!!!!',(40,50))
	elif self.error ==15:
		self.label = wx.StaticText(self, -1,'Check whether required fields are filled properly !!!!!',(40,50))

		
	self.label.SetFont(font1)



       	#self.st1 = wx.StcText(self, -1, 'alert message ')
       	#self.st1.SetFont(font)

        self.Centre()
	self.element =[]
    def OnClose(self, event):
        self.Close(True)




