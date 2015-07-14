#!/usr/bin/python
import os
import requests
import tarfile
import gzip
import sys
import subprocess

def main():
    if not os.path.exists('/var/lib/pacman/sync'):
        raise FileNotFoundError('Do you use Arch? Try running pacman -Syu.')
    url = 'https://aur.archlinux.org/packages.gz'
    r = requests.get(url, stream=True)
    if r.status_code != 200:
        print("HTTP response error, status code %d." % r.status_code)
        sys.exit()
    gz = str(r.content).split('\\n')
    mylist = []
    for i in range(1, len(gz)-1):
        mylist.append(gz[i])
    length = len(mylist)
    print("Found {0} AUR packages.".format(len(mylist)))
    sh_mylist = []
    output = subprocess.getoutput("pacman -Ss | grep '^[a-z]'")
    output = output.split("\n")
    for item in output:
        mylist.append(item.split("/")[1].split(" ")[0])
    mylist = sorted(set(mylist))
    with open(os.path.expanduser('~')+'/.pkglist', 'w+') as my_file:
        for item in mylist:
            my_file.write(item+"\n")
    with gzip.open(os.path.expanduser('~')+'/.pkglist.gz', 'wb') as gout:
        my_file = open(os.path.expanduser('~')+'/.pkglist', 'rb')
        gout.writelines(my_file)
    print("Completed successfully. {0} packages found; {1} AUR and {2} packages in official repositories. {3} duplicates.".format(len(mylist),length,len(output),(len(output)+length) - len(mylist)))

if __name__ == "__main__":
    main()
