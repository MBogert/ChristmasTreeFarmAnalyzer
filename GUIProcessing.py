from tkinter import *
import json
import requests 
import io
import config # Follow README for instructions on using API Key
import Variables

def validateAcreage(userInput):
	if not(userInput in '0123456789.') or (int(userInput) <= 0):
		return Variables.invalidAcreage
	else:
		return Variables.validInput


def validateAge(userInput):
	if not(userInput in '0123456789') or (int(userInput) <= 0) or (float(userInput) % int(userInput) > 0):
		return Variables.invalidAge
	else:
		return Variables.validInput

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
		return Variables.invalidAddress
	# Otherwise, retrieve lat/lon from json and return
	else:
		return Variables.validInput


def evaluateGeoCodeQuality(qualityCode):
	# Determine confidence of the geo code's quality (this could be enhanced, as it only checks granularity)
	granularity = qualityCode[:2]
	if(granularity in Variables.validGranularity):
		print("Valid geocode") #Debug
		return true
	else:
		print("Invalid geocode") #Debug
		return false


def returnLatLon(jsonFile):
	# Open reader and load json file
	f = io.open(jsonFile, 'r', encoding='utf-8-sig')
	data = json.load(f)

	# Retrieve lat/lon values from the json file
	for element in data['results']:
		for location in element['locations']:
			for field,value in location.items():
				if "latLng" in field: 
					# Return value
					f.close(jsonFile)
					return ("Lat: " + value["lat"] + ", Lng: " + value["lng"])
	# Indicates no Lat/Lng values in the json
	return "NULL"

def processInput(age, acreage, address, breed):
	# Retrieve Values
	print("Starting Input Processing")

	# Validate
	print("Checking validation")
	validation = validateInput(age, acreage, address)

	if(validation != Variables.validationMessages[Variables.validInput]):
		return validation
	else:
		print("Do stuff")

def validateInput(age, acreage, address):
	print("Starting validation Check")

	# Return Validation Codes
	ageCheck = validateAge(age)
	acreCheck = validateAcreage(acreage)
	addressCheck = validateAddress(address)

	# Check Codes and return message appropriately
	if(ageCheck != Variables.validInput):
		return Variables.validationMessages[ageCheck]
	elif(acreCheck != Variables.validInput):
		return Variables.validationMessages[acreCheck]
	elif(addressCheck != Variables.validInput):
		return Variables.validationMessages[addressCheck]
	else:
		return Variables.validationMessages[Variables.validInput]

	




	

