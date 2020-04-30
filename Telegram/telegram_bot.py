import requests
import time

access_token = ''

class TGBot(object):
	def __init__(self, access_token):
		self.access_token = access_token
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/getUpdates'		
		self.response = requests.get(self.ping_url).json()
		self.chat_id = self.response['result'][0]['message']['chat']['id']
		self.number_of_messages = len(self.response['result'])
		self.new_message = []
		#return self.chat_id

	def send_message(self,message):
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/sendMessage?'+\
					'chat_id='+str(self.chat_id)+'&parse_mode=Markdown'+'&text='+message
		self.response = requests.get(self.ping_url)

	def send_photo(self,filepath):
		file_ = open(filepath,"rb")
		file_dict = {'photo':file_}
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/sendPhoto?'+\
					'chat_id='+str(self.chat_id)
		self.response = requests.post(self.ping_url,files=file_dict)
		file_.close()

	def check_new_message(self):
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/getUpdates'
		self.response = requests.get(self.ping_url).json()
		if len(self.response['result']) > self.number_of_messages:
			for i in range(len(self.response['result'])-self.number_of_messages):
				self.new_message.append(self.response['result'][self.number_of_messages+i]['message']['text'])
			self.number_of_messages = len(self.response['result'])
		print(self.new_message)

if __name__ == '__main__':
	bot = TGBot(access_token)
	bot.send_message('Hurray!!')
	#bot.send_photo('/mnt/d/bracelet2.JPG') 
	stime = time.time()
	while time.time()-stime<2:
		print('Waiting...')
		#bot.send_message('Hurray!!')
		#bot.send_photo('telegraph.jpg') 
	bot.check_new_message()

	#Appropriate file name for windows needs to be given
