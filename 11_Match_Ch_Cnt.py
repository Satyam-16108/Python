def count(str1 ,str2) :
	set_string1 = set(str1)
	set_string2 = set(str2)

	matched_characters = set_string1 & set_string2

	print("No. of matching characters are : " + str(len(matched_characters)) )
	print("Matching characters are : " , matched_characters )
	print(type(matched_characters))
if __name__ == "__main__" :

	str1 = input("Enter STring 1 : ")
	str2 = input("Enter STring 2 : ")

	count( str1 , str2 )