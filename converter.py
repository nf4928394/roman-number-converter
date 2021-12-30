# Function that converts a Roman numeral to a regular number.
# COMPLETED
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
# IN PROGRESS. Function needs to be completed and tested before being marked complete.
def numToRoman(int):
	roman = ""
	map_ones = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
	map_tens = {1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
	map_hunds = {1:"C", 2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC",9:"CM"}
	map_thous = {1:"M", 2:"MM", 3:"MMM"}

	placelist = ("ones", "tens", "hunds", "thous")
	numdict = {}
	int_hold = int
 	for i in placelist: # Breaks int_hold into separate values for ones, tens, hundreds, and thousands place. Stores in numdict.
		numdict[i] = int_hold % 10
		int_hold //= int_hold

	for j in placelist: # Appends Roman numerals to the string 'roman' based on the values stored in numdict and the four hash maps above.
        if numdict[j] != 0:
        	roman = numdict[j] + roman

# Function that receives user input, performs error control, calls one of the two functions above, and prints out the returned conversion.  
# IN PROGRESS. Function needs to be completed and tested before being marked complete.
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
