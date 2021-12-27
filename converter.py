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

# Function that receives user input, performs error control, and prints out the returned conversion.  
def receiveUserInput():
	user_input = input("Please enter your Roman numeral or number here: ")
	try:
		test = int(user_input)
	except:
		print("You've entered the string:", user_input)
		result = romanToNum(user_input)
		print(
	
	result = numToRoman(
	
# Execution of receiveUser() function
print('''

	||| ROMAN NUMERAL/NUMBER CONVERTER |||
			||| By nf4928394 |||

	Welcome! This program converts a Roman numeral to a standard number, or a standard number to a Roman numeral.

	Restrictions:

	--The number (or number equivalent, if entering a Roman numeral) must fall between 1 and 3999.

	--If entering a number, it must be an integer (i.e. no decimal places). The number will automatically round down if any decimals are present.

	--If entering a Roman numeral, it must be a string and must only contain the following letters: I, V, X, L, C, D, M.

	--If entering a Roman numeral, it must be formatted such that letters are by decreasing value (e.g. XXVI), unless
	denoting numbers 4 (IV), 9 (IX), 40 (XL), 90 (XC), etc.
	______________________________________________________________''')
receiveUserInput()
