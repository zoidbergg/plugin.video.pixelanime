# -*- coding: utf-8 -*-
import os,requests,urllib,urllib2,re
import sys
import unicodedata
import doctest
import urlparse
import cgi
import random
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
def HentaiV2():
	url = "https://www.animakai.info/hentai/page/1"
	r = requests.get(url, headers)
	next_pageID = (url.rsplit('/', 1)[-1])
	s = int(next_pageID) + 1
	in_page="https://www.animakai.info"
	next_page = "https://www.animakai.info/hentai/page/%d"%s
	matched = re.compile(u'(?s)(?<=<div class=\"nome-thumb-anime\">).*?(?=<\/div>)', re.DOTALL | re.UNICODE).findall(r.content)
	for match in matched:
		img = re.compile(u'<img src="(.+?)" alt="" class="img-full" />', re.DOTALL | re.UNICODE).findall(match)
		_match = re.compile(u'<a href="(.+?)" title="(.+?)" class="thumb">', re.DOTALL | re.UNICODE).findall(match)
		for url, name in _match:
			print name
			_url = in_page+url
			print _url
		for _img in img:
			__img = ''.join(_img)
			print __img
	print next_page
			
def InsideHentaiV2():
	url ="http://anituga.xyz/"
	r = requests.get(url, headers)

	matchedTOP2 = re.compile(u'<div class=\"skoro-img img-box pseudo-link\" data-link=\"(.+?)\">.+?<img src=\"(.+?)\" alt=\"(.+?)\" />', re.DOTALL).findall(r.content)
	
	#for match in matchedTOP1: 
	#	_match = re.compile(u'<a class="carouside-item" href="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />', re.DOTALL).findall(match)
	for url, img, name in matchedTOP2:
		print name
		print img
		print url
	#matchTOP1 = re.compile(u'(?s)(?<=<div id=\"owl-carouside\">).*?(?=<div class=\"sidebox\">)', re.DOTALL).findall(r.content)
	#for match in matchTOP1: 
	#	_match = re.compile(u'<a class="carouside-item" href="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />', re.DOTALL).findall(matchTOP1)
	#		for _url, _img, _name in _match:
	#	date = re.compile(u'<span class="Dat2">(.+?)</span>').findall(match)
	#	url = re.compile(u'<a href="(.+?)">') .findall(match)
	#	for img, name in _match: 
	#		_name= name.replace("&#8211","")
	#		_date = ''.join(date)
	#		url = ''.join(url)
	#		print _name
	#print match

def PlayHentaiV2(url):
	r = requests.get(url, headers)
	matched = re.compile(u'(?s)(?<=<div class=\"box-video visible-sm visible-xs\">).*?(?=<\/div>)', re.DOTALL | re.UNICODE).findall(r.content)
	for match in matched:
		_match = re.compile(u'<video alt=\"(.+?)\" controls preload=\"none\" width=\"100%\" height=\"100%\" poster=\"(.+?)\"', re.DOTALL | re.UNICODE).findall(match)
		url = re.compile(u'<source src=\"(.+?)\"', re.DOTALL | re.UNICODE).findall(match)
		for name, img in _match:
			print name
			print img
		for _url in url:
			print _url

			
url=None
InsideHentaiV2()
