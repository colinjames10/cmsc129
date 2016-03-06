import sys
import re #For importing regex

def getHammingDistance(str1,str2):
	if(len(str1) == len(str2) and len(str1) > 0 and len(str2) > 0):						#Checks first if the strings have the same length
		hd = 0;
		for index in range(len(str1)):				#Traverses through each index then iterates hd if not equal
			if(str1[index] != str2[index]):
				hd+= 1
		print(hd)
		
	else:
		print("Strings must be greater than 0 and equal in length!")
		

def countSubstrPattern(original, pattern):			#Uses re.finditer to check for the pattern in original
	print (len([a for a in re.finditer('(?=' + pattern + ')', original)]))
													#(?=pattern) is used for overlapping substrings
def isValidString(str, alphabet):
	for letter in str:								#Traverses to the string and compares each of them to the letters in the alphabet
		bool = False
		for letter2 in alphabet:
			if(letter == letter2):
				bool = True
				break;
		if(bool == False):	return print(bool);		#If a letter in the str didn't equal to any of the letters in the alphabet, it will return false
	return print(bool);

def getSkew(str, n):								#Returns the number of Gs minus the number of Cs
	if(len(str) > 0):								#Checks if string length and n is greater than 0
		if(n > 0 || n > len(str)):
			g = 0
			c = 0
			for index in range(n):
				if(str[index] == 'G'): g+=1			#Gets all Gs and Cs from the string up to nth index then returns difference
				if(str[index] == 'C'): c+=1
			return print(g-c)						
		else:
			print("Second parameter is invalid!")
	else:
		print("Strings must be greater than 0 in length!")

def getMaxSkewN(str, n):
	if(len(str) > 0):								#Checks if string length and n is greater than 0
		if(n > 0 || n > len(str)):
			g = 0
			c = 0
			for index in range(len(str)):
				if(str[index] == 'G'): g+=1			#Gets all Gs in the string
			for index in range(n):					#Gets all Cs from the string up to nth index then returns difference
				if(str[index] == 'C'): c+=1
			return print(g-c)						
		else:
			print("Second parameter is invalid!")
	else:
		print("Strings must be greater than 0 in length!")
eval(sys.argv[1])