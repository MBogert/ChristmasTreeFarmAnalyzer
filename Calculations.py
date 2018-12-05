import Variables
import math

# Absorption for a set of trees at maximum maturity
def totalMaxAnnualAbsorption(acres):
	return (acres * Variables.tonsPerAcre)

# Absorption for a set of trees for a specific year
# Fits rate to function: absorption = year * x^2
# Year is year of growth, x is some constant fitted to the maximum rate
def absorptionForYear(acres, year):
	maxAbsorption = totalMaxAnnualAbsorption(acres)
	modifier = math.sqrt(maxAbsorption / Variables.averageYears)
	return (year * math.pow(modifier, 2))
