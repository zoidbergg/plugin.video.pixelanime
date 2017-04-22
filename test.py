import os,requests,urllib,urllib2,re
import sys
import unicodedata
import doctest
import urlparse
import cgi
import random

def Random():
	i = 1
	number =  random.randint(0,664)
	url_random ='http://anituga.xyz/index.php?newsid=%s'%number
	r = requests.get(url_random)
	image = re.compile('(?s)(?<=<div class=\"movie-poster\">).*?(?=<\/div>)').findall(r.content)
	normal1 = unicode(image[0], "utf-8")
	rline = unicodedata.normalize('NFC', normal1).encode('utf8','ignore')
	regex = re.compile('<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(str(rline))
	
	for image, name in regex:
		print name
		print image

	match = re.compile('<source src="(.+?)"').findall(r.content)
	for url in match:
		print url
		i += 1


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

Random()
#cat1("http://anituga.xyz/index.php?cstart=1&do=cat&category=misterio")