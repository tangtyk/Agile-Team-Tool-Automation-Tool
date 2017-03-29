import wx
import json
import attFrame
import requests
import staticValue
import excelOutput

class GenerateFrame(attFrame.ATTFrame):

	def __init__(self, parent = None, title = None, sid = None):
		attFrame.ATTFrame.__init__(self)
		self.sid = sid
		panel = wx.Panel(self, -1)
		wx.StaticText(panel, -1, 'Welcome! Press Generate to get report', pos = (190, 42))
		self.generateButton = wx.Button(panel, -1, 'Generate', pos=(245, 120))
		self.Bind(wx.EVT_BUTTON, self.onGenerate, self.generateButton)

		self.json_url_dic = staticValue.dic
		self.iteration_url = staticValue.iteration_url
		self.cookieHeaders = {}
		self.excelOutput = excelOutput.ExcelOutput()

	"""press Generate button to generate report"""
	def onGenerate(self, evt):
		self.statusbar.SetStatusText('Generating...', 0)
		if self.excelOutput.write_data_to_execel(self.getJson()):
			dlg = wx.MessageDialog(self, 'Generated successfully!', 'Done', wx.OK)
			dlg.ShowModal()
			dlg.Destroy()
		self.statusbar.SetStatusText('', 0)

	def getJson(self):
		self.cookieHeaders['Cookie'] = self.sid
		responseJsonList = []
		for team_id in self.json_url_dic.keys():
			"""get json once have got the sid"""
			# responseJsonDict[json_url[69:]] = json.loads(requests.get(json_url, headers=self.cookieHeaders).text)
			responseJsonList.extend(json.loads(requests.get(self.iteration_url + team_id, headers=self.cookieHeaders).text))
		return responseJsonList