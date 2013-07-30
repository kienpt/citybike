import urllib
import json
import sys

#This call provides a list of the networks supported in CityBikes
def getNW():
	#Init Returns
	name2url = {} # Map name of the network to it's url

	url = 'http://api.citybik.es/networks.json'
	try:
		jsondata = urllib.urlopen(url).read()
		js = json.loads(jsondata)
		for nw in js:
			name2url[nw['name']] = nw['url']
		return name2url
        except urllib.URLError:
                print ("URLLIB ERROR")
                return "URLLIB Error"
        except:
                return "Unexpected Error"


def getStationStatus(networkName):
	#Init Returns
	res = ''

	url = 'http://api.citybik.es/' + networkName  + '.json'
	try:
		jsondata = urllib.urlopen(url).read()
        	js = json.loads(jsondata)
		for station in js:
			line = station['name'] + '\t' +\
				str(station['idx']) + '\t' +\
				station['timestamp'] + '\t' +\
	                        str(station['number']) + '\t' +\
        	                str(station['free']) + '\t' +\
                	        str(station['bikes']) + '\t' +\
                        	station['coordinates'] + '\t' +\
	                        str(station['lat']) + '\t' +\
        	                str(station['lng']) + '\t' +\
                	        str(station['id'] )
			res = res + '\n' + line
		return res.strip('\t')
	except urllib.URLError:
                print ("URLLIB ERROR")
                return "URLLIB Error"
	except:
		return "Unexceptional Error"

 
def testGetNW():
	print 'TESTING GET NETWORK...'
	n2u = getNW()
	print "Number of networks: " + str(len(n2u))
	print "URL to citibike NYC: " + n2u['citibikenyc']
	print "List all of networks: "
	s = ''
	for key in n2u.keys():
		s = s + ", " + key
	print s.strip(',')

def testGetSS():
	print 'TESTING GET STATION STATUS...'
	print getStationStatus('citibikenyc')

if __name__=='__main__':
	testGetNW()
	testGetSS()
