# -*- coding: utf-8 -*-
import os,requests,urllib,urllib2,re
import sys
import unicodedata
import doctest
import urlparse
import cgi
import random
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
r = requests.get("http://www.animesonline.online/boku-no-hero-academia-2-episodio-04", headers)
matched = re.compile('<source src="(.+?)" type="video/mp4">', re.DOTALL).findall(r.content)
_matched = re.compile("file: '(.+?)',label: '720p',type: 'mp4'").findall(r.content)
for url in matched:
	_url = url
	print _url
		#addLink(_url,_url, '', '', '')
for url2 in _matched:
		#addLink(url2,url2, '', '', '')
	print url2