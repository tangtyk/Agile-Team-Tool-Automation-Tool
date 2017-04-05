
class TimedOutException(Exception):  
    def __init__(self, err='Request timed out'):  
        Exception.__init__(self, err)

class LoginErrorException(Exception):  
	def __init__(self, err='Your w3id or password was entered incorrectly.'):  
		Exception.__init__(self, err)

class FirefoxDriverErrorException(Exception):  
	def __init__(self, err='Firefox Driver configuration incorrect.'):  
		Exception.__init__(self, err)