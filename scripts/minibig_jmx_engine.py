from urllib2 import urlopen
from urllib2 import URLError
import json

#Return the item position number or 254 value if not found
def get_metricscategory_position(jsonbeansdata, lookupcategory):
    pointer = 0
    while pointer < len(jsonbeansdata):
        catname = jsonbeansdata[pointer]['name']
        if catname == lookupcategory:
            return pointer
        pointer += 1
    return 254

def load_jmx(urlregionserver):
    #print urlregionserver
	try:
		rsjmx = urlopen(urlregionserver)
		rsdata = str(rsjmx.read())
		rsjson = json.loads(rsdata)
		rsbeans = rsjson['beans']
		return rsbeans
	except URLError, e:
		print "Server at "+urlregionserver+" can't be reached.:"+str(e)
		exit(1)
	else:
		print "Server:"+urlregionserver+" can't be contacted."
		exit(1)
