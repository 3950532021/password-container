# save password
import json
from difflib import get_close_matches
data={"website": "github.com", "username": "1379", "password": "1"}

def getData():
	data={}
	data["website"]=input("Enter your website address:")

	data["username"]=input("Enter your user name:")

	data["password"]=input("Enter your password:")
	return data
def writeData(data):
	
	file=open("data.txt")
	jdata=json.load(file)
	jdata["sites"].append(data)
	file.close()
	file=open("data.txt","w+")
	json.dump(jdata,file)
	file.close()

def readData(website=None):
	file=open("data.txt","r")
	sites=json.load(file)
	file.close()
	if(website):
		for site in sites["sites"]:
			if site["website"]==website:
				return site
	else:
		return sites

def printResult(data):
	for x in data:
		print(x,":",data[x])
		print("")
	print("<<<<job successfully done>>>>")

def askName():
	siteName=input("enter website name:")
	sites=readData()
	siteNames=[]
	for site in sites["sites"]:
		siteNames.insert(0,site["website"])
	
	if len(get_close_matches(siteName,siteNames))>0:
		
		yn=input("did you mean %s ?y/n   "%get_close_matches(siteName,siteNames)[0])
		if (yn=="y"):
			return {"status":"200","data":get_close_matches(siteName,siteNames)[0]}
		else:
			yn=input("its new site?y/n")
			if yn=="y":
				return {"status":"202","data":[]}
	else:
		yn=input("its new site?y/n")
		if yn=="y":
			return {"status":"202","data":[]}
while(True):
	site=askName()
	
	if  (site["status"]=="200"):
		printResult(readData(site["data"]))
	elif (site["status"]=="202") :
		writeData(getData())








