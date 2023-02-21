"""Get transcriptions
"""

from bs4 import BeautifulSoup as bs
import re
from requests import get
import sys
import binascii
import os


def get_soup(query_url):
    # cache using query_url as name basis, per
    # https://stackoverflow.com/questions/27253530/save-url-as-a-file-name-in-python
    s = binascii.hexlify(query_url.encode()).decode("utf-8")
    fname = os.path.join('cache', s)

    # Don't cache page/#, which are the listings of the transcriptions and can change.
    if "page" in query_url:
        print(f'Getting listing {query_url}')
        if os.path.exists(fname):
            os.remove(fname)

    if not os.path.exists(fname):
        print(f'caching call to {query_url}')
        raw = get(query_url).content.decode('utf-8')
        with open(fname, 'w') as f:
           f.write(raw)
    else:
        print(f'cache hit for {query_url}')

    raw = None
    with open(fname, 'r') as f:
        raw = f.read()
    soup = bs(raw, features='html.parser')
    return soup


def get_links(soup):
    anchors = soup.find_all('a', {'itemprop': 'url'})
    def is_transcription(a):
        href = a['href']
        if href.endswith('-transcripcion'):
            return True
        if href.find('transcripcion/transcripcion') != -1:
            return True
        return False
    tas = [a for a in anchors if is_transcription(a)]
    urls = [a['href'] for a in tas]
    # print(urls)
    return urls

def get_transcription(soup):
    t = soup.select('div.qode-post-text-main')[0]
    return t.text.strip()

def get_all_transcriptions_listed_on(url):
    soup = get_soup(url)
    urls = get_links(soup)
    for u in urls:
        saveasbase = u.split('/')[-1]
        soup = get_soup(u)
        t = get_transcription(soup)
        fname = os.path.join('transcripciones', f'{saveasbase}.txt')
        print(f'File: {fname}')
        with open(fname, 'w') as f:
            f.write(t)
    
if __name__ == '__main__':
    baseurl = 'https://radioambulante.org/category/transcripcion'
    for i in range(1, 16):
        get_all_transcriptions_listed_on(f'{baseurl}/page/{i}')
