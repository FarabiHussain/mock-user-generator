import logging, datetime, json


def write(msg):
	filename = str(datetime.datetime.now()).split(".")[0] + ".json"
	
	with open(filename, "w") as outfile: 
		json.dump(msg, outfile, indent=4)