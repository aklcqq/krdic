#!python3
import urllib.request, urllib.parse, urllib.error
import ssl
#import re
import json
#import time

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from bs4 import BeautifulSoup

#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

## def

# convert to utf8
def get_id(vocab):
    rawurl = 'https://zh.dict.naver.com/api3/zhko/tooltip?query='
    vocab = urllib.parse.quote(vocab, safe='/',encoding='utf-8')
    url = rawurl + vocab
    uhp = urllib.request.Request(url, headers=hdr)
    uh = urllib.request.urlopen(uhp, context=ctx)
    data = uh.read().decode()
#    data = data.rstrip()
    datajs = json.loads(data.rstrip())

#    jsre = datajs['jsonResult']
    datajsre = datajs['jsonResult'][0]
    word_id = datajsre['entryId']
    return word_id


## ignore ssl certificate error

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

hdr = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

fn = input('Enter file name: ')
fh = open(fn)
sfh = open('saveid.txt','a')
for vocab in fh:
    try:
        word_id = get_id(vocab)
        sfh.write(word_id + '\n')
    except:
        print('NOT FOUND:'+ vocab)
sfh.close()

