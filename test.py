# -*- coding: utf-8 -*-
import os,requests,urllib,urllib2,re
import sys
import unicodedata
import doctest
import urlparse
import cgi
import random

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

def insidev2():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
	site = "http://www.animesorion.tv/23091"
	image ="http://3.bp.blogspot.com/-TgoHF3txaT8/VZG7-e-YWnI/AAAAAAAAavc/SB_Hv1sA0X8/s420/Dragon-Ball-Super.jpg"
	r = requests.get(site, headers)
	#Get the sourrce of movie in V2
	match = re.compile('(?s)(?<=ul class=\"lcp_catlist\" id=\"lcp_instance_0\">).*?(?=<\/ul>)').findall(r.content)
	_match = unicodedata.normalize('NFC', unicode(str(_match), "utf-8")).encode('utf8','ignore')
	__match = re.compile('<a href=\"(.+?)\" title=\"(.+?)\">',re.DOTALL).findall(str(_match))
	for url, name in __match:
		print name
		print url


def InsideDBS():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
	r = requests.get("http://www.animesorion.tv/", headers)
	#next_page = re.compile('<span class="pnext"><a href="(.+?)"><span class="fa fa-angle-double-right"></span></a></span>',re.DOTALL).findall(r.content)
	match = re.compile('(?s)(?<=<div class=\"cAlign\">).*?(?=<\/ul>)').findall(r.content)
	#_match = re.compile('(?s)(?<=<div class=\"Titulotelinhas\">).*?(?=<\/div>)',re.DOTALL).findall(str(match))
	#__match = re.compile('<a href="(.+?)" title="(.+?)">').findall(str(_match))
	_match = re.compile('(?s)(?<=<div class=\"Titulotelinhas\">).*?(?=<\/div>)').findall(str(match))
	__match = re.compile('<a href="(.+?)" title="(.+?)">',re.DOTALL).findall(str(_match))
	#image = re.compile('<img src="(.+?)" title="(.+?)" alt="(.+?)"><\/a>').findall(str(__match))
	#for image, name2, name3 in image:
	#	_image = image
	for url, name in __match:
		#name2 = unicodedata.bidirectional('NFC', "Epis\\\\xc3\\\\xb3dio", "utf-8").decode('utf8','ignore')
		
		print name.decode('utf-8')
		#print url
		#addDir3(name, url, 9, '', '', '')
#InsideDBS()

#print u"%s"%name.encode('raw_unicode_escape').decode('utf-8')

r = requests.get("http://www.animesorion.tv/page/3")
match = re.compile('(?s)(?<=<div class=\"cAlign\">).*?(?=<\/ul>)',re.DOTALL).findall(r.content)
image = re.compile('<img src="(.+?)"').findall(str(match))
_match = re.compile('(?s)(?<=<div class=\"Titulotelinhas\">).*?(?=<\/div>)',re.DOTALL).findall(str(match))
__match = re.compile('<a href="(.+?)" title="(.+?)">').findall(str(_match))

for _image in image:
	print _image
	#for url, name in __match:
		#addDir3(name, url, 9, '', __image, '')
	#addDir3("Next Page", str(next_page), 19, '','http://i.imgur.com/a3TSg6N.jpg','')