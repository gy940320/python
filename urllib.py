import urllib2
def html(url):
	html=urllib2.urlopen(url).read()
	return html
	url='http://www.baidu.com'
	print html(url)
