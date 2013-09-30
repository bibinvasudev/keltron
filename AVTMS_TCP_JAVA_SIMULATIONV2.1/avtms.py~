import os
import wx
import time
import threading
import avtmscorefull
import avtmscorehalf
import math
import sys
from socket import *
import datetime
import random
import alert


class avtms(wx.Frame):
	def __init__(self, parent, id, title):
#creating GUI
		wx.Frame.__init__(self, parent, id, title, wx.Point(400,200), wx.Size(450,350))
		self.Centre()
		self.Show()
		liss = []
		self.__toolset()

	def __toolset(self):
		font = wx.Font(13, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'UnDotum')
		font1 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u'UnDotum')
   
		self.SetBackgroundColour(wx.Colour(31,123,15))
		self.label = wx.StaticText(self, -1, '                       AVTMS SIMULATOR',(20,20))
		self.label.SetFont(font)

		self.label2 = wx.StaticText(self, -1, 'IP ADDRESS     ',(20,70))
		self.label2.SetFont(font1)

		self.label3 = wx.StaticText(self, -1, 'PORT NUMBER ',(20,115))
		self.label3.SetFont(font1)

		self.label1 = wx.StaticText(self, -1, 'SELECT FILE',(20,170))
		self.label1.SetFont(font1)

		self.label12 = wx.StaticText(self, -1, 'TIME INTERVEL',(20,215))
		self.label12.SetFont(font1)

		self.textbox1 = wx.TextCtrl(self, -1, "",(120,67),(175,25))
		self.textbox2 = wx.TextCtrl(self, -1, "",(120,111),(175,25))

		self.textbox3 = wx.TextCtrl(self, -1, "",(120,165),(175,25))
		self.textbox4 = wx.TextCtrl(self, -1, "",(120,209),(175,25))

		self.textbox1.SetBackgroundColour(wx.Colour(217,217,217))
		self.textbox2.SetBackgroundColour(wx.Colour(217,217,217))
		self.textbox3.SetBackgroundColour(wx.Colour(217,217,217))
		self.textbox4.SetBackgroundColour(wx.Colour(217,217,217))

		self.button_connect=wx.Button(self,555,'CONNECT',(300,110),(120,30))
		self.button_connect.SetBackgroundColour(wx.Colour(163, 162, 164))
		self.button_select=wx.Button(self,111,'SELECT',(300,165),(120,30))
		self.button_select.SetBackgroundColour(wx.Colour(163, 162, 164))

		self.button_run=wx.Button(self,222,'RUN FULLMODE ',(20,260),(130,40))
		self.button_run.SetBackgroundColour(wx.Colour(163, 162, 164))

		self.button_run1=wx.Button(self,666,'RUN HALFMODE ',(160,260),(130,40))
		self.button_run1.SetBackgroundColour(wx.Colour(163, 162, 164))		



		self.button_stop=wx.Button(self,333,'STOP',(300,260),(130,40))
		self.button_stop.SetBackgroundColour(wx.Colour(163, 162, 164))

		wx.EVT_BUTTON(self,111,self.ButtonSelectPressed)
		wx.EVT_BUTTON(self,555,self.ButtonConnectPressed)

		wx.EVT_BUTTON(self,666,self.ButtonRunhalfPressed)
		wx.EVT_BUTTON(self,222,self.ButtonRunPressed)

		wx.EVT_BUTTON(self,333,self.ButtonStopPressed)
		self.button_run.Disable()
		self.button_select.Disable()
		self.button_run1.Disable()

	def ShowMessage(self):
		wx.MessageBox(self.textbox.GetValue())
	def ButtonRunhalfPressed(self,event):

#Start working in half mode 
		c = len(liss)
		if not self.textbox4.GetValue():

			error = 10
			aler = alert.alert(None, -1,"ALERT MESSAGE!!!!!!!!!!!!",error)
        		aler.ShowModal()
        		return

		else:

			self.time_intervel = self.textbox4.GetValue()

		for inds in range(c):

			avtms1= avtmscorehalf.avtmscorehalf(liss[inds],self.s,self.time_intervel)
			avtms1.start()
		
	def ButtonConnectPressed(self,event):

		self.port =self.textbox2.GetValue()
		self.ip= self.textbox1.GetValue()

		if not self.textbox1.GetValue():

			error = 15
			aler = alert.alert(None, -1,"ALERT MESSAGE!!!!!!!!!!!!",error)
			aler.ShowModal()
			return

		elif not self.textbox2.GetValue() :

			error = 11
			aler = alert.alert(None, -1,"ALERT MESSAGE!!!!!!!!!!!!",error)
			aler.ShowModal()
			return

		# creaing tuple

		t = (self.ip,int(self.port))

		try:
			self.s = socket(AF_INET, SOCK_STREAM)
			self.s.connect(t)
			error = 3
			aler = alert.alert(None, -1,"        Connection success",error)
        		aler.ShowModal()
			self.button_select.Enable()
        		aler.Destroy()

		except:

			error = 1
			aler = alert.alert(None, -1,"ALERT MESSAGE!!!!!!!!!!!!",error)
        		aler.ShowModal()
			
        		aler.Destroy()

		
	def ButtonSelectPressed(self,event):

#selecting the file from direcories
		 files = ""
		 dlg = wx.FileDialog(self, message="Open File", defaultDir=os.getcwd(),style=wx.MULTIPLE) 
		 if dlg.ShowModal() == wx.ID_OK:
			 filename = dlg.GetPaths()
			 coun=len(filename)

			 for i in range(coun):

				files=files+filename[i]+";"
				liss .append(filename[i])

			 self.textbox3.SetValue(files)
			 dlg.Destroy()
			 cou=len(filename)
 			 self.button_run.Enable()
			 self.button_run1.Enable()
			 
	def ButtonRunPressed(self,event):

#start running in full mode ie continuous loop
		
		c = len(liss)
		if not self.textbox4.GetValue():
			error = 10
			aler = alert.alert(None, -1,"ALERT MESSAGE!!!!!!!!!!!!",error)
        		aler.ShowModal()
			return

		self.time_intervel = self.textbox4.GetValue()
		
		for inds in range(c):

			avtms = avtmscorefull.avtmscorefull(liss[inds],self.s,self.time_intervel)
			avtms.start()
			
	def ButtonStopPressed(self,event):

		sys.exit()

liss = []
app=wx.App()
avtms(None, -1, 'Stimulation')
app.MainLoop()
