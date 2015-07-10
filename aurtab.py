import os
import requests
import tarfile
import gzip
import sys

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
    tar_mylist = []
    for direc in os.listdir('/var/lib/pacman/sync'):
        tar = tarfile.open('/var/lib/pacman/sync/'+direc)
        t = tar.getmembers()
        tar_mylist.append(t)
    for i in range(0, len(tar_mylist)-1):
        for thing in tar_mylist[i]:
            if "/" in thing.name:
                mylist.append(thing.name.split("/")[0])
            else:
                mylist.append(thing.name)
    mylist = sorted(set(mylist))
    with open(os.path.expanduser('~')+'/.pkglist', 'w+') as my_file:
        for item in mylist:
            my_file.write(item+"\n")
    with gzip.open(os.path.expanduser('~')+'/.pkglist.gz', 'wb') as gout:
        my_file = open(os.path.expanduser('~')+'/.pkglist', 'rb')
        gout.writelines(my_file)
if __name__ == "__main__":
    main()
