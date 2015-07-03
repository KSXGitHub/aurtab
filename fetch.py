from bs4 import BeautifulSoup
import requests
import re

class buildDB(object):
	#check version colour and author(orphan) in future, thread for data fetching + another for writing?
    def __init__(self):
        self.site = 'https://aur.archlinux.org/packages/?O=0&K=&PP=250'
        self.r = requests.get(self.site, stream=True)
        self.soup = BeautifulSoup(self.r.content)
        print(self.soup.prettify)

    def get_list(self):
        temp_array = self.soup.find_all('p',limit=2)[1].string
        a = re.sub(r"[\n]?[\t]+","",temp_array).split('.')
        b = a[1].split(' ')
        limit = int(b[len(b)-1])
        for i in range(0,limit+1):
            self.site = 'https://aur.archlinux.org/packages/?O='+str(250*i)+'&K=&PP=250'
            self.r = requests.get(self.site, stream=True)
            self.soup = BeautifulSoup(self.r.content)
            rows = self.soup.html.body.find_all('tr')
            for row in rows:
                row = row.find_all('a',limit=1)
                d = re.sub(r">(.*)<\/a>","",str(row))
                print(row)
                print(d)
                print('{}'.format(i*250))
