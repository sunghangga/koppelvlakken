import requests
from bs4 import BeautifulSoup
import os, datetime, time
import wget
import urllib2


def get_source():
    archive_url = 'https://data.ndovloket.nl/cxx/'
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content,'html.parser')
    
    links = soup.findAll('a')

    max_time = 0
    current_file = ''

    for link in links:
        if link['href'].endswith('zip'):
            u = urllib2.urlopen(archive_url+link['href'])
            meta = u.info()
            meta_modifiedtime = time.mktime(datetime.datetime.strptime( \
                                ''.join(meta.getheaders("Last-Modified")), "%a, %d %b %Y %X GMT").timetuple())

            if max_time < meta_modifiedtime:
                max_time = meta_modifiedtime
                current_file = archive_url+link['href']
    return current_file

def download_source(link):
    path = 'src'
    if not os.path.exists (path):
        os.makedirs(path)

    file_name = link.split('/')[-1]
    if os.path.exists ('%s/%s' % (path, file_name)):
        print 'Source file is up to date'
    else:
        # remove all file in directory
        for z_file in os.listdir(path):
            os.remove(os.path.join(path, z_file))
        
        # Checking if the directory is empty or not 
        if not os.listdir(path):
            wget.download(link, '%s/%s' % (path, file_name))

# Download new source file
link = get_source()
download_source(link)
