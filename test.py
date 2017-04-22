import os,requests,urllib,urllib2,re
import sys
import unicodedata
import doctest
import urlparse
import cgi

def cat1(url):
	url2 = url
	r = requests.get(url)
	match = re.compile('<div class="movie-img img-box pseudo-link" data-link="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	for url, image, name  in match:
		print (name)
	next(url2)

def next(url):
	r = requests.get(url)
	next_page = re.compile('<span\sclass="pnext"><a\shref="(.+?)"><span\sclass="fa\sfa-angle-double-right"></span></a></span>').findall(r.content)
	next_page2 = ''.join(next_page)
	next_page2 = next_page2.replace("&lt;", "<")
	next_page2 = next_page2.replace("&gt;", ">")
	next_page2 = next_page2.replace("&amp;", "&")
	if next_page2:
		print next_page2
		cat1(next_page2)
	else:
		print("finish")

#cat1("http://anituga.xyz/index.php?cstart=1&do=cat&category=misterio")
cat1("http://anituga.xyz/index.php?cstart=1&do=cat&category=misterio")