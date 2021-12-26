# Function that converts a Roman numeral to a regular number.
def romanToNum(str):
	map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} # Hash map used to calculate numerical values for Roman letters.
	val = 0 # Used to store the ongoing total.
	for i in range(len(str)):
		if i + 1 < len(str) and map[str[i]] < map[str[i+1]]:
			val -= map[srt[i]]
			else:
			val += map[srt[i]]
	return val

# Function that converts a number to a Roman numeral.
def numToRoman(int):

# Code that receives user input and prints out the returned conversion.  
