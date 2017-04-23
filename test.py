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
	_match = unicodedata.normalize('NFC', unicode(match[0], "utf-8")).encode('utf8','ignore')
	__match = re.compile('<a href=\"(.+?)\" title=\"(.+?)\">',re.DOTALL).findall(str(_match))
	for url, name in __match:
		print name
		print url

def v12():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
	r = requests.get('http://anituga.xyz/v/index.php?cstart=1&', headers)
	match = re.compile('<a class="item-link" href="(.+?)">.+?<img class="xfieldimage poster" src="(.+?)" alt="" />.+?<div class="item-title">(.+?)</div>',re.DOTALL).findall(r.content)
	#for  url, image, name in match:
		#print name
		#print image
		#print url
		#v2(url)
	print(r.content)
insidev2()
#cat1("http://anituga.xyz/index.php?cstart=1&do=cat&category=misterio")Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36