import urllib
import lxml.html

get=raw_input("Enter the Url link \n")
connection = urllib.urlopen(get)

fo = open("url.txt", "wb")
dom =  lxml.html.fromstring(connection.read())
for link in dom.xpath('//a/@href'): 
	print link
	fo.write(link)
	fo.write("\n")
fo.close()	