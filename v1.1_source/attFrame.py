#coding=utf-8
import wx

ID_ABOUT = 200

class ATTFrame(wx.Frame):

	def __init__(self, parent = None, title = None):
		wx.Frame.__init__(self, parent, -1, 'ATT Automation Tool', size = (600, 300), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP)
		self.SetMaxSize((600, 300))
		self.SetMinSize((600,300))
		self.Center()
		self.icon = wx.Icon('ATTtool.ico', wx.BITMAP_TYPE_ICO)
		self.SetIcon(self.icon)
		self.menuBar = wx.MenuBar()
		self.menu = wx.Menu()
		self.menuBar.Append(self.menu, 'Help')
		self.menu.Append(ID_ABOUT, 'About', 'About')
		self.SetMenuBar(self.menuBar)
		# self.Bind(wx.EVT_MENU, self.onAbout, ID_ABOUT)
		wx.EVT_MENU(self, ID_ABOUT, self.onAbout)
		self.statusbar = self.CreateStatusBar(2)
		self.statusbar.SetStatusText('IBM Confidential', 1)

	def onAbout(self, evt):
		dlg = wx.MessageDialog(self, 'ATT Automation Tool\n© Copyright IBM Corporation 2017\nAll Rights Reserved\nVersion: 1.0, powered by SPRT team\nContact us:\nlizhiwcd@cn.ibm.com\ntyktang@cn.ibm.com', 'About ATT Automation Tool', wx.OK)
		dlg.ShowModal()
		dlg.Destroy()
		# description = 'ATT Automation Tool is an internal tool to generate/get report from site:Agile Team Tool\nVersion: 1.0, powered by SPRT team\nContact us:\nlizhiwcd@cn.ibm.com\ntyktang@cn.ibm.com'
		# info = wx.AboutDialogInfo()
		# info.SetIcon(wx.Icon('superman_48px.ico',wx.BITMAP_TYPE_PNG))
		# info.SetDescription(description)
		# info.SetCopyright('© 2017 - 2017 Lee&Calvin')
		# wx.AboutBox(info)