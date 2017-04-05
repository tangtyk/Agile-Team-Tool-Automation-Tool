import loginFrame
import generateFrame

class GUIManager():
	
	def __init__(self, UpdateUI):
		self.UpdateUI = UpdateUI

	"""retrun one of the 2 frames by type"""
	def GetFrame(self, type, sid = None):
		if type == 0:
			return loginFrame.LoginFrame(UpdateUI = self.UpdateUI)
		elif type == 1:
			return generateFrame.GenerateFrame(sid = sid)