# Function that converts a Roman numeral to a regular number.
def romanToNum(str):
	map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} # Hash map used to calculate numerical values for Roman letters.
	val = 0 # Used to store the ongoing total.
	for i in range(len(str)):
		if i + 1 < len(str) and map[str[i]] < map[str[i+1]]:
			val -= map[str[i]]
		else:
			val += map[str[i]]
	return val

# Function that converts a number to a Roman numeral. 
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
def receiveUserInput(inp):
	try: # Checks to see if 'inp' is an integer or float.
		conv1 = float(inp)
		conv2 = int(conv1)
		result = numToRoman(conv2)
		print("______________________________________________________________")
		print("\nYou entered the number:", inp)
		print("The Roman numeral for this number is: "+result+"\nIf your number contained a decimal, it was rounded down before converting.")
	except: # Runs if 'inp' is a string.
		try:
			result = romanToNum(inp)
			print("______________________________________________________________")
			print("\nYou entered the Roman numeral:", inp)
			print("The numerical version of this Roman numeral is:", result)
		except: # Runs if the string 'inp' is formatted incorrectly.
			print("______________________________________________________________")
			print("\nError; incorrect input. Please make sure that you're entering a number or a Roman numeral.")

	print("\nIf you'd like to run a new conversion, please enter a new number or Roman numeral below.")
	print("Otherwise, type \"end\" in all lowercase to quit the program.")
	inp2 = input("")
	if inp2 == "end": # Ends program if user inputs "end."
		quit()
	else:
		receiveUserInput(inp2)
	
# Initial message and execution of receiveUserInput() function.
print('''

||| ROMAN NUMERAL/NUMBER CONVERTER by nf4928394 -- Version 1.0 |||

Welcome! This program converts a Roman numeral to a standard number, and vice-versa.


Restrictions:

--The number/Roman numeral must have a value between 1 and 3999.

--If entering a number, it will automatically round down if any decimals are present.

--If entering a Roman numeral, it must only contain the uppercase letters I, V, X, L, C, D, and M.
______________________________________________________________''')
inp = input("\nPlease enter your Roman numeral or number here: ")
receiveUserInput(inp)
