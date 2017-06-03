import sys
from lxml import html
import requests
import urlparse
import os
from progressbar import *
import subprocess

def process_links(links):
    x=[]
    for l in links:
        if(l[-3:]=="gif"):
                x.append(l)
    return x

m = list()
g = list()
num_lines = sum(1 for line in open('url.txt'))
for line in file('url.txt'):
	if line.strip():
		print "-->",list(line.strip().split())
		m.append(list(line.strip().split()))
print num_lines
for index in range(num_lines):
	g=m[index]
	st = '\n'.join(g)
	print (st)
	URL = st
        page = requests.get(URL)
        tree = html.fromstring(page.text)
        img = tree.xpath('//img/@src')
        links = tree.xpath('//a/@href')
        img_links =  process_links(links)
        img.extend(img_links)
	#print img

info=open('tmp.txt','a')
for ele in img:
	ele.split(",")	
	info.write(ele+"\n")
#info.write("\n\n\n\n\n\n")
#info.close()	

if len(img)==0:
	sys.exit( "Sorry, no images found")
        print "Found %s images: "%len(img)
        no_to_download =len(img) 

subprocess.call(['wget','-i','tmp.txt','--directory-prefix=Images/','picz'])