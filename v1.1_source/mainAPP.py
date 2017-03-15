import wx
import guiManager

class MainAPP(wx.App):

	def OnInit(self):
		self.manager = guiManager.GUIManager(self.UpdateUI)
		"""create login frame"""
		self.frame = self.manager.GetFrame(0)
		self.frame.Show(True)
		return True	

	def UpdateUI(self, type, sid):
		self.frame.Close()
		self.frame = self.manager.GetFrame(type, sid)
		self.frame.Show(True)

def main():
    app=MainAPP()
    app.MainLoop()

if __name__=="__main__":
	main()
