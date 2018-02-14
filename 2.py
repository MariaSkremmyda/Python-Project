import urllib2
import json
import datetime

def kinoo(UserList=[], Results=[]):
	counter=0
	for i in xrange(10):
		for j in xrange(20):
			if UserList[i]==Results[j]:
				counter+=1
	return counter

cur_date=datetime.datetime.now()
	
mynums = raw_input("Give me 10 comma separated values:\n\t")
mynums = mynums.split(',')
WrongInput = 0
for i in xrange(len(mynums)):
	if int(mynums[i])<1 or int(mynums[i])>80 or len(mynums[i])>2:
		WrongInput+=1
while len(mynums)!=10 or WrongInput>0:
	mynums = raw_input("Wrong Input, try to give me 10 valid comma separated values this time:\n\t")
	mynums = mynums.split(',')
	WrongInput=0
	for i in xrange(10):
		if mynums[i]<1 or mynums[i]>80 or type(mynums)!='int':
			WrongInput+=1 

for i in xrange(10):
	mynums[i]=int(mynums[i])

succDates = []
successes = []
for i in range(31):
	cur_date = cur_date - datetime.timedelta(days=1)
	date_str = cur_date.strftime("%d-%m-%Y")
	url ='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
	req = urllib2.Request(url)
	response = urllib2.urlopen(req) 
	data = response.read()
	dataDict = json.loads(data)
	response.close()
	klhrwseis = dataDict['draws']['draw']
	r = 0
	for k in klhrwseis:
		tmp = k["results"]
		if kinoo(mynums, tmp)>4:
			r+=1
	print str(r) + " epityxies stis: " + date_str
	successes.append(r)
	succDates.append(date_str)
success=successes[0]
succDate=succDates[0]
for i in xrange(1,31):
	if successes[i]>success:
		success=successes[i]
		succDate=succDates[i]
print "\n\n\tThe best day for the given combination was: " + succDate