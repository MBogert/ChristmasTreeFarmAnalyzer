from tkinter import *
import json
import requests 

def validateAcreage(userInput):
	if not(userInput in '0123456789.') or (int(userInput) <= 0):
		print("ACREAGE MUST BE EXPRESSED IN A POSITIVE NUMBER")

def validateAddress(userInput):
	# Use MapQuest's API to retrieve Lat/Lon
	# Build GET call
	getCall = "http://open.mapquestapi.com/geocoding/v1/address?"
	key = "key=KEY" # TODO Figure out how to encrypt the key
	location = "&location=" + userInput

	# Make the request
	response = requests.get(getCall)

	# Verify response didn't return an error