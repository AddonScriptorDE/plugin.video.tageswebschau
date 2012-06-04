#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib,urllib2,re,xbmc,xbmcgui

def getUrl(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

content=getUrl("http://www.tagesschau.de/tageswebschau/")
match=re.compile('<meta name="DC.Date" content="(.+?)T', re.DOTALL).findall(content)
date=match[0]
splDate=date.split("-")
listitem = xbmcgui.ListItem('TagesWEBschau vom '+splDate[2]+'.'+splDate[1]+'.'+splDate[0])
xbmc.Player().play("http://httpmedia.radiobremen.de/twsdl/"+date+"_tws_L.mp4",listitem)
