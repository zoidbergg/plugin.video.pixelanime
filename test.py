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

def insidev2():
	r = requests.get("http://anituga.xyz/v/index.php?newsid=150")
	#Get the sourrce of movie in V2
	match = re.compile('<iframe src=\"(.+?)\" scrolling=\"no\" frameborder=\"0\" width=\"890\" height=\"501\" allowfullscreen></iframe>').findall(r.content)
	for url in match:
		#addDir3("Episode %d"%(i), url, 1, '', '', '')
		#Play video and put the episode number
		print url

def v12():
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	r = requests.get('http://anituga.xyz/v/index.php?cstart=1&', headers)
	match = re.compile('<a class="item-link" href="(.+?)">.+?<img class="xfieldimage poster" src="(.+?)" alt="" />.+?<div class="item-title">(.+?)</div>',re.DOTALL).findall(r.content)
	#for  url, image, name in match:
		#print name
		#print image
		#print url
		#v2(url)
	print(r.content)
v12()
#cat1("http://anituga.xyz/index.php?cstart=1&do=cat&category=misterio")