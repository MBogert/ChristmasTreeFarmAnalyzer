from tkinter import *
import json
import requests 
import io
import config # Follow README for instructions on using API Key

def validateAcreage(userInput):
	if not(userInput in '0123456789.') or (int(userInput) <= 0):
		print("ACREAGE MUST BE EXPRESSED IN A POSITIVE NUMBER")

def validateAddress(userInput):
	# Use MapQuest's API to retrieve Lat/Lon
	# Build GET call
	getCall = "http://open.mapquestapi.com/geocoding/v1/address?"
	key = "key=" + config.mapAPI # Follow README for instructions on using API Key
	location = "&location=" + userInput

	# Make the request and load the json into a reader
	response = requests.get(getCall)
	f = io.open(response, 'r', encoding='utf-8-sig')
	data = json.load(f)

	# Retrieve the GeoCode quality value from the json file
	geoCodeQuality = ""
	for element in data['results']:
		for location in element['locations']:
			for field,value in location.items():
				if "geocodeQualityCode" in field: 
					geoCodeQuality = value
					break
	print(geoCodeQuality) # For test/debug 

	# Close reader
	f.close(response)

	# If the GeoCode quality is insufficient, throw an error
	if not(evaluateGeoCodeQuality(geoCodeQuality)):
		print("ERROR: ADDRESS INVALID")
	# Otherwise, retrieve lat/lon from json and return
	else:
		print("Need to return address")

def evaluateGeoCodeQuality(qualityCode):
	print("Fill")

# Assumes file is already opened
def returnLatLon(jsonFile):
	print ("Fill")
