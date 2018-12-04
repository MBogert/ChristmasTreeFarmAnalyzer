from tkinter import *

def validateAcreage(userInput):
	if not(userInput in '0123456789.') or (int(userInput) <= 0):
		print("ACREAGE MUST BE EXPRESSED IN A POSITIVE NUMBER")