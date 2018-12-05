# Breeds of Trees
breeds = {"Balsalm Fir", "Fraser Fir", "Canaan Fir", "Douglass Fir", "Grand Fir", "Noble Fir", "Concolor Fir", "White Pine", "Scotch Pine", "Virginia Pine", "Blue Spruce", "Norway Spruce", "White Spruce", "Arizona Cypress", "Leyland Cypress", "Red Cedar"}

# CO2 Absorption Rates
# From http://www.realchristmastrees.org/dnn/portals/22/Documents/carbon.pdf
# And another study TODO Determine how to cite study in codebase
# tonsPerAcreDouglassFir = 5.8 # Assumes 5 ft tall Douglass Firs with 5x5 spacing
tonsPerAcre = 12 # Assumes 7 ft tall Fraser Firs with 5x5 spacing <-- DEFAULT NUMBER FOR VERSION 1

# Average Years to Maturity
averageYears = 7

# Valid GeoCode Quality Codes for addresses
# P1
# L1
# I1
# B1
# B2
# B3
validCodes = {}
invalidCode = "X"