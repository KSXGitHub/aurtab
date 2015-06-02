from bs4 import BeautifulSoup
import requests

class buildDB(object):
	#check version colour and author(orphan) in future, thread for data fetching + another for writing?
	def __init__(self):
		site = 'https://aur.archlinux.org/packages/?O=0&K=&PP=250'
		r = requests.get(site, stream=True)
		soup = BeautifulSoup(r.content)
		print(soup.prettify)

	def get_list(self):
		temp_array = self.soup.find_all('p',limit=2)[1].string
		a = str(temp_array[1])
		b = a.split(' ')
		limit = b[len(b)-1].split('.')[0]
		for i in range(0,limit+1):
			site = 'https://aur.archlinux.org/packages/?O='+str(250*i)+'&K=&PP=250'
			r = requests.get(site, stream=True)
			soup = BeautifulSoup(r.content)
			rows = soup.find_all('tr')
			for row in rows:
				print(soup.find_all('a'))
