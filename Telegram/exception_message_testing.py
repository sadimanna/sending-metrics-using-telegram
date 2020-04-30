import requests
import time

access_token = ''

class TGBot(object):
	def __init__(self, access_token):
		self.access_token = access_token
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/getUpdates'		
		self.response = requests.get(self.ping_url).json()
		self.chat_id = self.response['result'][0]['message']['chat']['id']
		#return self.chat_id

	def send_message(self,message):
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/sendMessage?'+\
					'chat_id='+str(self.chat_id)+'&parse_mode=Markdown'+'&text='+message
		self.response = requests.get(self.ping_url)

if __name__ == '__main__':
	bot = TGBot(access_token)
	bot.send_message('Exception Message Testing!!')

	try:
		printf(1/0)
	except Exception as ex:
		template = "An exception of type {0} occurred.\nArguments:\n{1!r}"
    	message = template.format(type(ex).__name__, ex.args)
    	bot.send_message(message)
	
