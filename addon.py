# -*- coding: utf-8 -*-
import xbmcaddon
import os
import requests
import xbmc
import xbmcgui
import urllib
import urllib2
import re
import xbmcplugin
import sys
import unicodedata
import random

#Adicionar Menu
def MENU():
	addDir3("Popular",'s',5,'http://i.imgur.com/6Iwsjq0.png','http://i.imgur.com/a3TSg6N.jpg','Popular')
	addDir3("Categorias",'s',6,'http://i.imgur.com/pTcI3jz.png','http://i.imgur.com/a3TSg6N.jpg','Categorias.')
	addDir3("Series Orientais",'s',13,'http://i.imgur.com/iy0spNY.png','http://i.imgur.com/a3TSg6N.jpg','')
	addDir3("Series Ocidentais",'s',14,'http://i.imgur.com/eZXUVgX.png','http://i.imgur.com/a3TSg6N.jpg','')
	addDir3("Filmes Orientais",'s',15,'http://i.imgur.com/iy0spNY.png','http://i.imgur.com/a3TSg6N.jpg','')
	addDir3("Filmes Ocidentais",'s',16,'http://i.imgur.com/eZXUVgX.png','http://i.imgur.com/a3TSg6N.jpg','')
	addDir3("Episodios Recentes", 'http://www.animesonline.online/page/1', 8,'http://i.imgur.com/N3COLLn.png','http://i.imgur.com/a3TSg6N.jpg','Recents')
	addDir3("Random Anime", 's', 12,'http://i.imgur.com/5awo5tw.png','http://i.imgur.com/a3TSg6N.jpg','Random')
	addDir3("Hentai", 's', 10, 'http://i.imgur.com/Xg25LSL.png','http://i.imgur.com/a3TSg6N.jpg',"Para maiores de 18 anos.")
	addDir3("HentaiV2", 'https://www.animakai.info/hentai/page/1', 20, 'http://i.imgur.com/Xg25LSL.png','http://i.imgur.com/a3TSg6N.jpg',"Para maiores de 18 anos.")
	addDir3("A-Z",'s',7,'http://i.imgur.com/OdwGEPM.png','http://i.imgur.com/a3TSg6N.jpg','A-Z')
####################################### HENTAI V2 ##########################################################################
#23
def PlayHentaiV2(url):
	r = requests.get(url, headers)
	matched = re.compile(u'(?s)(?<=<div class=\"box-video visible-sm visible-xs\">).*?(?=<\/div>)', re.DOTALL | re.UNICODE).findall(r.content)
	for match in matched:
		_match = re.compile(u'<video alt=\"(.+?)\" controls preload=\"none\" width=\"100%\" height=\"100%\" poster=\"(.+?)\"', re.DOTALL | re.UNICODE).findall(match)
		url = re.compile(u'<source src=\"(.+?)\"', re.DOTALL | re.UNICODE).findall(match)
		for _url in url:
			__url =_url
		for name, img in _match:
			addLink(name, __url, img, '', img)
#22
def InsideHentaiV2(url):
	r = requests.get(url, headers)
	in_page="https://www.animakai.info"
	matched = re.compile(u'(?s)(?<=<div class=\"nome-thumb\">).*?(?=<\/div>)', re.DOTALL | re.UNICODE).findall(r.content)
	for match in matched:
		_match = re.compile(u'<a href="(.+?)" title="(.+?)" class="tt">', re.DOTALL | re.UNICODE).findall(match)
		img = re.compile(u'<img src="(.+?)" alt="" class="img-full" />', re.DOTALL | re.UNICODE).findall(match) 
		for _img in img:
			__img = ''.join(_img)
		for url, name in _match:
			_next_page = in_page + url
			#__next_page = ''.join(_next_page)
			addDir3(name, _next_page, 23, __img, __img, '')
#21	
def NextPageHentaiV2(url):
	r = requests.get(url, headers)
	HentaiV2(url)
#20
def HentaiV2(url):
	r = requests.get(url, headers)
	next_pageID = (url.rsplit('/', 1)[-1])
	s = int(next_pageID) + 1
	next_page = "https://www.animakai.info/hentai/page/%d"%s
	in_page="https://www.animakai.info"
	matched = re.compile(u'(?s)(?<=<div class=\"nome-thumb-anime\">).*?(?=<\/div>)', re.DOTALL | re.UNICODE).findall(r.content)
	for match in matched:
		img = re.compile(u'<img src="(.+?)" alt="" class="img-full" />', re.DOTALL | re.UNICODE).findall(match)
		_match = re.compile(u'<a href="(.+?)" title="(.+?)" class="thumb">', re.DOTALL | re.UNICODE).findall(match)
		for _img in img:
			__img = ''.join(_img)
		for url, name in _match:
			_url = in_page + url
			addDir3(name, _url, 22, __img, __img, '')
	if next_page:
		addDir3("Next Page", next_page, 21,'','http://i.imgur.com/a3TSg6N.jpg','')
#############################################################################################################################
#18
def InsideDBS(url):
	image ="https://upload.wikimedia.org/wikipedia/en/thumb/7/74/Dragon_Ball_Super_Key_visual.jpg/220px-Dragon_Ball_Super_Key_visual.jpg"
	r = requests.get(url, headers)
	date = re.compile(u'<p>Publicado Dia: <span>(.+?)/span></p>').findall(r.content)
	_date = ''.join(date)
	#thumbnail = re.compile(u'<meta property="og:image" content="(.+?)"\/>').findall(r.content)
	match = re.compile("<source src=\"(.+?)\" type='video/mp4' />").findall(r.content)
	#for _thumbnail in thumbnail:
	#	__thumbnail = _thumbnail
	for url in match:
		addLink("Play - %s"%_date, url, image, '', image)
#17
def DragonBallSuper():
	site = "http://www.animesorion.tv/23091"
	image ="https://upload.wikimedia.org/wikipedia/en/thumb/7/74/Dragon_Ball_Super_Key_visual.jpg/220px-Dragon_Ball_Super_Key_visual.jpg"
	r = requests.get(site, headers)
	match = re.compile('(?s)(?<=ul class=\"lcp_catlist\" id=\"lcp_instance_0\">).*?(?=<\/ul>)').findall(r.content)
	_match = unicodedata.normalize('NFC', unicode(match[0], "utf-8")).encode('utf8','ignore')
	__match = re.compile('<a href=\"(.+?)\" title=\"(.+?)\">',re.DOTALL).findall(str(_match))
	for url, name in __match:
		addDir3(name, url, 18, image, image, '')
#16
def FilmesOcidental():
	#Url
	site = "http://anituga.xyz/filmes-ocidentais"
	#Get all html content of site 
	r = requests.get(site, headers)
	match = re.compile('<div class="movie-img img-box pseudo-link" data-link="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	#Get the next page link
	next_page = re.compile('<span class="pnext"><a href="(.+?)"><span class="fa fa-angle-double-right"></span></a></span>',re.DOTALL).findall(r.content)
	for  url, image, name in match:
		addDir3(name, url, 3, image, image, '')
	#Checks if next_page is empty, if there is a next page add a directory 
	if next_page:
		addDir3("Next Page", site, 11,'','http://i.imgur.com/a3TSg6N.jpg','')
#15
def FilmesOriental():

	site = "http://anituga.xyz/filmes-orientais"
	r = requests.get(site, headers)
	match = re.compile('<div class="movie-img img-box pseudo-link" data-link="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	next_page = re.compile('<span class="pnext"><a href="(.+?)"><span class="fa fa-angle-double-right"></span></a></span>',re.DOTALL).findall(r.content)
	for  url, image, name in match:
		addDir3(name, url, 3, image, image, '')
	if next_page:
		addDir3("Next Page", site, 11,'','http://i.imgur.com/a3TSg6N.jpg','')
#14
def SeriesOcidental():
	site = "http://anituga.xyz/series-ocidentais"
	r = requests.get(site, headers)
	match = re.compile('<div class="movie-img img-box pseudo-link" data-link="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	next_page = re.compile('<span class="pnext"><a href="(.+?)"><span class="fa fa-angle-double-right"></span></a></span>',re.DOTALL).findall(r.content)
	for  url, image, name in match:
		addDir3(name, url, 3, image, image, '')
	if next_page:
		addDir3("Next Page", site, 11,'','http://i.imgur.com/a3TSg6N.jpg','')
#13
def SeriesOriental():
	site = "http://anituga.xyz/series-orientais"
	r = requests.get(site, headers)
	match = re.compile('<div class="movie-img img-box pseudo-link" data-link="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	next_page = re.compile('<span class="pnext"><a href="(.+?)"><span class="fa fa-angle-double-right"></span></a></span>',re.DOTALL).findall(r.content)
	for  url, image, name in match:
		addDir3(name, url, 3, image, image, '')
	if next_page:
		addDir3("Next Page", site, 11,'','http://i.imgur.com/a3TSg6N.jpg','')
#12
def Random():
	#Generate a random number from 5 to 664
	number =  random.randint(5,664)
	#Append the generated number to url, to get a random movie link
	url_random ='http://anituga.xyz/index.php?newsid=%s'%number
	#Call a function to process the random movie link
	InsideMovie(url_random)
#10
def Hentai():
	site = "http://anituga.xyz/index.php?cstart=1&do=cat&category=hentai"
	r = requests.get(site, headers)
	match = re.compile('<div class="movie-img img-box pseudo-link" data-link="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	next_page = re.compile('<span class="pnext"><a href="(.+?)"><span class="fa fa-angle-double-right"></span></a></span>',re.DOTALL).findall(r.content)
	for  url, image, name in match:
		addDir3(name, url, 3, image, image, '')
	if next_page:
		addDir3("Next Page", site, 11,'','http://i.imgur.com/a3TSg6N.jpg','')
################################ RECENTS #####################################################################################
#19
def NextPageV2(url):
	r = requests.get(url, headers)
	LastEp(url)
#9
def InsideMovieV2(url):
	r = requests.get(url, headers)
	matched = re.compile('<source src="(.+?)" type="video/mp4">', re.DOTALL).findall(r.content)
	_matched = re.compile("file: '(.+?)',label: '720p',type: 'mp4'").findall(r.content)
	thumbnail =re.compile('<img class="alignleft wp-image-18348 size-thumbnail" title="(.+?)" src="(.+?)"').findall(r.content)
	for name,img in thumbnail:
		_name = name
		_img = img
	i=1
	for url in matched:
		_url = url
		addLink(_name+' | Source %d'%i,_url, _img, '', _img)
		i += 1
	for url2 in _matched:
		addLink(_name+' | Source HD',url2, _img, '', _img)
#8
def LastEp(url):
	r = requests.get(url, headers)
	next_pageID = (url.rsplit('/', 1)[-1])
	s = int(next_pageID) + 1
	next_page = "http://www.animesonline.online/page/%d"%s
	matched = re.compile(u'(?s)(?<=<div class=\"capa\">).*?(?=</a>)', re.DOTALL).findall(r.content) 
	for match in matched: 
		_match = re.compile(u'<img style="display: inline;" src="(.+?)" alt="(.+?)"', re.DOTALL).findall(match)
		date = re.compile(u'<span class="Dat2">(.+?)</span>').findall(match)
		url = re.compile(u'<a href="(.+?)">') .findall(match)
		for img, name in _match: 
			_name= name.replace("&#8211","")
			_date = ''.join(date)
			url = ''.join(url)
			addDir3(str(_date)+" | "+str(_name), url, 9, img, img, '')
	addDir3("Next Page", str(next_page), 19, '','http://i.imgur.com/a3TSg6N.jpg','')
###############################################################################################################################
#7
def CategoriasAZ():
	r = requests.get('http://anituga.xyz', headers)
	#Parse A-Z categories
	match = re.compile('(?s)(?<=<div class=\"flex-row\">).*?(?=<\/div>)',re.DOTALL).findall(r.content)
	#Normalize content
	_match = unicodedata.normalize('NFC', unicode(match[0], "utf-8")).encode('utf8','ignore')
	#Get name and url of Category
	regex = re.compile('<a href=\"(.+?)\">(.+?)</a>',re.DOTALL).findall(str(_match))
	for  url, name in regex:
		addDir3(name, 'http://anituga.xyz%s'%url, 4, '','http://i.imgur.com/a3TSg6N.jpg','')
#6
def Categorias():
	r = requests.get('http://anituga.xyz', headers)
	match = re.compile('(?s)(?<=<ul class=\"hidden-menu clearfix\">).*?(?=<\/ul>)',re.DOTALL).findall(r.content)
	_match = unicodedata.normalize('NFC', unicode(match[0], "utf-8")).encode('utf8','ignore')
	regex = re.compile('<a href=\"(.+?)\">(.+?)</a>',re.DOTALL).findall(str(_match))
	for  url, name in regex:
		addDir3(name, 'http://anituga.xyz%s'%url, 4, '','http://i.imgur.com/a3TSg6N.jpg','')
#5		
def Popular():
	r = requests.get('http://anituga.xyz', headers)
	imageDB ="https://upload.wikimedia.org/wikipedia/en/thumb/7/74/Dragon_Ball_Super_Key_visual.jpg/220px-Dragon_Ball_Super_Key_visual.jpg"
	match = re.compile('<a class="carou-item img-box" href="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	#DB Legendado
	addDir3("Dragon Ball Super (Legendado)", 'dbs', 17, imageDB, imageDB,'' )
	#TOP DOBRADOS
	matchedTOP1 = re.compile(u'<div class=\"skoro-img img-box pseudo-link\" data-link=\"(.+?)\">.+?<img src=\"(.+?)\" alt=\"(.+?)\" />', re.DOTALL).findall(r.content)
	for url1, img1, name1 in matchedTOP1:
		addDir3(name1, url1, 3, img1, img1, '')
	#TOP LEGENDADOS
	matchedTOP2 = re.compile(u'(?s)(?<=<div id=\"owl-carouside\">).*?(?=<div class=\"sidebox\">)', re.DOTALL).findall(r.content)
	for _match in matchedTOP2: 
		__match = re.compile(u'<a class="carouside-item" href="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />', re.DOTALL).findall(_match)
		for _url, _img, _name in __match:
			addDir3(_name, _url, 3, _img, _img, '')
	#Normal
	for  url, image, name in match:
		addDir3(name, url, 3, image, image, '')
#4
def InsideCategory(url):
	url2 = url
	r = requests.get(url, headers)
	match = re.compile('<div class="movie-img img-box pseudo-link" data-link="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	next_page = re.compile('<span\sclass="pnext"><a\shref="(.+?)"><span\sclass="fa\sfa-angle-double-right"></span></a></span>').findall(r.content)
	for url, image, name  in match:
		addDir3(name, url, 3, image, image, '')
	if next_page:
		addDir3("Next Page", url2, 11, '','http://i.imgur.com/a3TSg6N.jpg','')
#11
def NextPage(url):
	#Get html content
	r = requests.get(url, headers)
	#Get next page link
	next_page = re.compile('<span\sclass="pnext"><a\shref="(.+?)"><span\sclass="fa\sfa-angle-double-right"></span></a></span>').findall(r.content)
	#Kinda convert list to string
	next_page2 = ''.join(next_page)
	#EscapingHtml
	next_page2 = next_page2.replace("&lt;", "<")
	next_page2 = next_page2.replace("&gt;", ">")
	next_page2 = next_page2.replace("&amp;", "&")
	#Verify if link exists
	if next_page2:
		InsideCategory(next_page2)
#3 
def InsideMovie(url):
	#Counter to print episode number
	i = 1
	r = requests.get(url, headers)
	#Get source of video
	image = re.compile('(?s)(?<=<div class=\"movie-poster\">).*?(?=<\/div>)').findall(r.content)
	normal1 = unicode(image[0], "utf-8")
	rline = unicodedata.normalize('NFC', normal1).encode('utf8','ignore')
	regex = re.compile('<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(str(rline))
	for image, name in regex:
		image2=image
	match = re.compile('<source src="(.+?)"').findall(r.content)
	for url in match:
		#addDir3("Episode %d"%(i), url, 1, '', '', '')
		#Play video and put the episode number
		addLink(name+" - Episode %d"%(i), url, image2, '', image2)
		i += 1
#1 Function to play video
def PLAY(url):
	addLink(url, url, '', '', '')
#PLAY VIDEO		
def addLink(name,url,image,urlType,fanart):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
	liz.setProperty('fanart_image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
								
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param       
#Functions to Add directories  
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok     
def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
##################################################################################################################
def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % viewType )
        
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None
#User Agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

#Main Menu to call selected functions
if mode==None or url==None or len(url)<1:
        print ""
        MENU()
       
elif mode==1:
        PLAY(url)

elif mode==3:
        InsideMovie(url)

elif mode==4:
        InsideCategory(url)

elif mode==5:
		Popular()

elif mode==6:
		Categorias()

elif mode==7:
		CategoriasAZ()

elif mode==8:
		LastEp(url)
		
elif mode==9:
		InsideMovieV2(url)

elif mode==10:
		Hentai()

elif mode==11:
		NextPage(url)

elif mode==12:
		Random()

elif mode==13:
		SeriesOriental()

elif mode==14:
		SeriesOcidental()

elif mode==15:
		FilmesOriental()

elif mode==16:
		FilmesOcidental()

elif mode==17:
		DragonBallSuper()

elif mode==18:
		InsideDBS(url)

elif mode==19:
		NextPageV2(url)

elif mode==20:
		HentaiV2(url)

elif mode==21:
		NextPageHentaiV2(url)

elif mode==22:
		InsideHentaiV2(url)

elif mode==23:
		PlayHentaiV2(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))