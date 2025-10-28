import requests
class Client():
	def __init__(self):
		self.api="https://cataas.com"
	def random_cat(self):
		url=requests.get(f"{self.api}/cat/?json=true").json()["url"]
		return (f"{self.api}{url}")
	def get_says_cat(self,text:str):
		url=requests.get(f"{self.api}/cat/says/:{text}?json=true").json()["url"]
		return (f"{self.api}{url}")
	def get_cat_gif(self):
		return(f"{self.api}/cat/gif")