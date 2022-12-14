def count(filename):
	
	# Opening the file in read mode
	txt_file = open(filename, "r")

	# Initialize three variables to count number of vowels, lines and characters respectively
	vowel = 0
	line = 0
	character = 0

	# Make a vowels list so that we can check whether the character is vowel or not
	vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

	# Iterate over the characters present in file
	for alpha in txt_file.read():
		
		# Checking if the current character is vowel or not
		if alpha in vowels_list:
			vowel += 1
			
		# Checking if the current character is not vowel or new line character
		elif alpha not in vowels_list and alpha != "\n":
			character += 1
			
		# Checking if the current character is new line character or not
		elif alpha == "\n":
			line += 1

	# Print the desired output on the console.
	print("Number of vowels in ", filename, " = ", vowel)
	print("New Lines in ", filename, " = ", line)
	print("Number of characters in ", filename, " = ", character)

count('Myfile.txt')
