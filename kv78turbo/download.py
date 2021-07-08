import requests
from bs4 import BeautifulSoup
import os, datetime, time
import wget
import urllib2

def download_source(link):
    path = 'kv7planningdata'
    if not os.path.exists (path):
        os.makedirs(path)

    file_name = link.split('/')[-1]
    if os.path.exists ('%s/%s' % (path, file_name)):
        print 'Source file is up to date'
    else:
        wget.download(link, '%s/%s' % (path, file_name))

def get_source():
    # archive_url = 'https://data.ndovloket.nl/cxx/'
    archive_url = 'http://kv7.openov.nl/GOVI/KV7planning/'
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content,'html.parser')
    
    links = soup.findAll('a')

    max_time = 0

    for link in links:
        if link['href'].endswith('gz'):
            u = urllib2.urlopen(archive_url+link['href'])
            meta = u.info()
            meta_modifiedtime = datetime.datetime.strptime(''.join(meta.getheaders("Last-Modified")), "%a, %d %b %Y %X GMT").strftime('%Y')
            print(meta.getheaders("Last-Modified"))
            if meta_modifiedtime == '2021':
                # URL to archive file
                download_source(archive_url+link['href'])

# Download new source file
get_source()
