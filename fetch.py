from bs4 import BeautifulSoup
import requests
import re
import os
import string

class buildDB(object):
	#check version colour and author(orphan) in future, thread for data fetching + another for writing?
    def __init__(self):
        self.site = 'https://aur.archlinux.org/packages/?O=0&K=&PP=250'
        self.r = requests.get(self.site, stream=True)
        self.soup = BeautifulSoup(self.r.content)
       # if not os.path.isdir(os.path.expanduser('~')+".aurdb"):
       #     os.makedirs(os.path.expanduser('~')+"/.aurdb")
        if not (os.path.isdir(os.path.expanduser('~')+"/.packages")):
            os.makedirs(os.path.expanduser('~')+"/.packages")
            for char in string.ascii_lowercase+string.digits:
                os.makedirs(os.path.expanduser('~')+"/.packages/"+char)
        #else:

    def get_list(self):
        temp_array = self.soup.select("#pkglist-results > div > p:nth-of-type(1)")
        a = re.sub(r"[\n]?[\t]+","",temp_array[0].string).split('.')
        b = a[1].split(' ')
        limit = int(b[len(b)-1])
        for i in range(0,limit+1):
            self.site = 'https://aur.archlinux.org/packages/?O='+str(250*i)+'&K=&PP=250'
            self.r = requests.get(self.site, stream=True)
            self.soup = BeautifulSoup(self.r.content)
            names = self.soup.select(".results > tbody:nth-of-type(1) > tr > td:nth-of-type(2) > a")
            for name in names:
                fileObj = open((os.path.expanduser('~')) + "/.packages/"+name.string[0:1:]+"/"+name.string,'w')
                fileObj.close()
                #Write it to file
        #        out = open(os.path.expanduser('~') + "/.aurdb/" + name.string,'w')
        #        out.close()
