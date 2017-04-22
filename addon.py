import xbmcaddon,os,requests,xbmc,xbmcgui,urllib,urllib2,re,xbmcplugin
import sys
import unicodedata
import random

def MENU():
	addDir3("Popular",'popular',5,'http://megaicons.net/static/img/icons_sizes/358/999/256/retro-star-icon.png','','Series mais populares.')
	addDir3("Categorias",'cat',6,'http://i.imgur.com/pTcI3jz.png','','Categorias de Series e Filmes.')
	addDir3("Series Orientais",'cat',6,'','','')#
	addDir3("Series Ocidentais",'cat',6,'','','')#
	addDir3("Filmes Orientais",'cat',6,'','','')#
	addDir3("Filmes Ocidentais",'cat',6,'','','')#
	addDir3("Episodios Recentes", 'epa', 8,'','','')
	addDir3("Anime Aleatorio", 'ran', 12,'','','')
	addDir3("Hentai", 'hent', 10, 'http://i.imgur.com/Xg25LSL.png','',"Para maiores de 18 anos.")
	addDir3("A-Z",'cata',7,'','','')

#12
def Random():
	number =  random.randint(0,664)
	url_random ='http://anituga.xyz/index.php?newsid=%s'%number
	INSIDEmovie(url_random)

#10
def HentaiList():
	site = "http://anituga.xyz/index.php?cstart=1&do=cat&category=hentai"
	r = requests.get(site)
	match = re.compile('<div class="movie-img img-box pseudo-link" data-link="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	#Get the next page link
	next_page = re.compile('<span class="pnext"><a href="(.+?)"><span class="fa fa-angle-double-right"></span></a></span>',re.DOTALL).findall(r.content)
	for  url, image, name in match:
		addDir3(name, url, 3, image, '', '')
	#Checks if next_page is empty, if there is a next page and add directory if so
	if next_page:
		addDir("Next Page", site, 11,'')

#9
def INSIDEmovie2(url):
	r = requests.get(url)
	#Get the sourrce of movie in V2
	match = re.compile('<iframe src="(.+?)" scrolling="no" frameborder="0" width="890" height="501" allowfullscreen></iframe>').findall(r.content)
	for url in match:
		#addDir3("Episode %d"%(i), url, '', '', '', '')
		PLAY(url)

#8
def LastEp():
	r = requests.get('http://anituga.xyz/v/index.php?cstart=1&')
	match = re.compile('<a class="item-link" href="(.+?)">.+?<img class="xfieldimage poster" src="(.+?)" alt="" />.+?<div class="item-title">(.+?)</div>',re.DOTALL).findall(r.content)
	for  url, image, name in match:
		addDir3(name, url, 9, 'http://anituga.xyz%s'%image, '', '')

#7
def CategoriasAZ():
	r = requests.get('http://anituga.xyz')
	match = re.compile('(?s)(?<=<div class=\"flex-row\">).*?(?=<\/div>)',re.DOTALL).findall(r.content)
	normal1 = unicode(match[0], "utf-8")
	rline = unicodedata.normalize('NFC', normal1).encode('utf8','ignore')
	regex = re.compile('<a href=\"(.+?)\">(.+?)</a>',re.DOTALL).findall(str(rline))
	for  url, name in regex:
		addDir(name, 'http://anituga.xyz%s'%url, 4, '')
	

#6
def Categorias():
	r = requests.get('http://anituga.xyz')
	match = re.compile('(?s)(?<=<ul class=\"hidden-menu clearfix\">).*?(?=<\/ul>)',re.DOTALL).findall(r.content)
	# match = re.compile('(?s)(?<=<div class=\"flex-row\">).*?(?=<\/div>)',re.DOTALL).findall(r.content)
	normal1 = unicode(match[0], "utf-8")
	rline = unicodedata.normalize('NFC', normal1).encode('utf8','ignore')
	regex = re.compile('<a href=\"(.+?)\">(.+?)</a>',re.DOTALL).findall(str(rline))
	for  url, name in regex:
		addDir(name, 'http://anituga.xyz%s'%url, 4, '')
#5		
def Popular():
	r = requests.get('http://anituga.xyz')
	match = re.compile('<a class="carou-item img-box" href="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	for  url, image, name in match:
		addDir3(name, url, 3, image, '', '')

#4
def INSIDEcategorie(url):
	url2 = url
	r = requests.get(url)
	match = re.compile('<div class="movie-img img-box pseudo-link" data-link="(.+?)">.+?<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(r.content)
	next_page = re.compile('<span\sclass="pnext"><a\shref="(.+?)"><span\sclass="fa\sfa-angle-double-right"></span></a></span>').findall(r.content)
	for url, image, name  in match:
		addDir3(name, url, 3, image, '', '')
	if next_page:
		addDir("Next Page", url2, 11, '')
	
#11
def NextPage(url):
	#Get html content
	r = requests.get(url)
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
		INSIDEcategorie(next_page2)


#3 
def INSIDEmovie(url):
	#Counter to print episode number
	i = 1
	r = requests.get(url)
	#Get source of video
	image = re.compile('(?s)(?<=<div class=\"movie-poster\">).*?(?=<\/div>)').findall(r.content)
	normal1 = unicode(image[0], "utf-8")
	rline = unicodedata.normalize('NFC', normal1).encode('utf8','ignore')
	regex = re.compile('<img src="(.+?)" alt="(.+?)" />',re.DOTALL).findall(str(rline))
	for image, name in regex:
		image2=image
	match = re.compile('<source src="(.+?)"').findall(r.content)
	for url in match:
		#addDir3("Episode %d"%(i), url, '', '', '', '')
		#Play video and put the episode number
		addLink("Episode %d"%(i), url, image2, '', '')
		i += 1

#1 Function to play video
def PLAY(url):
		addLink('Play', url, '', '', '')


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
        INSIDEmovie(url)

elif mode==4:
        INSIDEcategorie(url)

elif mode==5:
		Popular()

elif mode==6:
		Categorias()

elif mode==7:
		CategoriasAZ()

elif mode==8:
		LastEp()
		
elif mode==9:
		INSIDEmovie2(url)

elif mode==10:
		HentaiList()

elif mode==11:
		NextPage(url)

elif mode==12:
		Random()

xbmcplugin.endOfDirectory(int(sys.argv[1]))