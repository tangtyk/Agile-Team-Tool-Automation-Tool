import wx
import time
import attFrame
import attExceptions
import staticValue
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class LoginFrame(attFrame.ATTFrame):

	def __init__(self, parent = None, title = None, UpdateUI = None):
		attFrame.ATTFrame.__init__(self)
		panel = wx.Panel(self, -1)
		self.w3Text = wx.StaticText(panel, -1, 'w3id:', pos = (160, 82))
		self.passwordText = wx.StaticText(panel, -1, 'password:', pos = (160, 122))
		wx.StaticText(panel, -1, 'Press Submit to login', pos = (230, 32))
		self.w3idCtrl = wx.TextCtrl(panel, -1, '', pos = (220, 80), size=(175,-1))
		self.passwordCtrl = wx.TextCtrl(panel, -1, '', pos = (220, 120), size=(175,-1), style=wx.TE_PASSWORD)
		self.submitButton = wx.Button(panel, -1, 'Submit', pos=(180, 150))
		self.cancelButton = wx.Button(panel, -1, 'Exit', pos=(300, 150))
		self.Bind(wx.EVT_BUTTON, self.onSubmit, self.submitButton)
		self.Bind(wx.EVT_BUTTON, self.onExit, self.cancelButton)
		self.UpdateUI = UpdateUI

		self.geckodriver_path = staticValue.dic['geckodriver_path']
		self.att_login_url = staticValue.dic['att_login_url']

	"""press Submit button to login"""
	def onSubmit(self, evt):
		self.statusbar.SetStatusText('Connecting... Please do not close the browser.', 0)
		try:
			driver = webdriver.Firefox(executable_path=self.geckodriver_path)
		except Exception as e:
			self.popMessageDialog('Your geckodriver setup is incorrect.', wx.ICON_ERROR)
			raise attExceptions.FirefoxDriverErrorException()
		
		driver.get(self.att_login_url)
		driver.find_element_by_id('desktop').send_keys(self.w3idCtrl.GetValue())
		driver.find_element_by_name('password').send_keys(self.passwordCtrl.GetValue())
		driver.find_element_by_id('btn_signin').click()
		time.sleep(3)
		self.statusbar.SetStatusText('', 0)
		try:
			driver.find_element_by_xpath('//p[@class="error"]')
		except NoSuchElementException as e:
			self.getSidFromCookie(driver)
		else:
			driver.close()
			driver.quit()
			self.popMessageDialog('Your w3id or password was entered incorrectly.', wx.ICON_ERROR)
			raise attExceptions.LoginErrorException()
			
	"""press Exit button to exit"""
	def onExit(self, evt):
		self.Close(True)

	def getSidFromCookie(self, driver):
		now = time.time()
		connect_sid = self.convertCookieToSid(driver.get_cookies())
		while connect_sid == None:
			if (time.time() - now) >60:
				self.popMessageDialog('Request timed out, please try again.', wx.OK)
				raise attExceptions.TimedOutException()
			time.sleep(5)
			connect_sid = self.convertCookieToSid(driver.get_cookies())
		"""redirect to generate frame"""
		self.UpdateUI(1, connect_sid)

	def convertCookieToSid(self, cookie):
		for item in cookie:
			if(item['name'] == 'connect.sid'):
				connect_sid = 'connect.sid=' + item['value']
				return connect_sid

	def popMessageDialog(self, message, type):
		dlg = wx.MessageDialog(self, message, 'Oops', type)
		dlg.ShowModal()
		dlg.Destroy()