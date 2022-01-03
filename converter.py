# Function that converts a Roman numeral to a regular number.
# Status: COMPLETED
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
# Status: COMPLETED
def numToRoman(int):
	roman = ""
	map2 = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
	100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM", 1000:"M", 2000:"MM", 3000:"MMM"}
	tenslist = [1, 10, 100, 1000]
	numlist = []

	for i in tenslist: # Breaks int_hold into separate values for ones, tens, hundreds, and thousands place. Stores in numdict.
		numlist.append(int % 10 * i)
		int //= 10

	for j in numlist: # Appends Roman numerals to the string 'roman' based on the values stored in numdict and the four hash maps above.
		if j != 0:
			roman = map2[j] + roman
	return roman

# Function that receives user input, performs error control, calls one of the two functions above, and prints out the returned conversion.  
# Status: IN PROGRESS; function needs to be completed and tested before being marked complete.
def receiveUserInput():
	user_input = input("Please enter your Roman numeral or number here: ")
	try:
		test = int(user_input)
	except:
		print("You've entered the string:", user_input)
		result = romanToNum(user_input)
	
# Execution of receiveUserInput() function.
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
